"""
aipmarc.py : internal AIP marc processing stuff : mark matienzo
"""

from string import Template
#from pymarc import format_field
import sys

def hip_url(bibno, catdb):
    """
    Creates URL to OPAC record from bib number and catalog database info.
    """
    u = 'http://libserv.aip.org:81/ipac20/ipac.jsp?uri=full=3100001~!'
    urltemplate = Template("%s${bibno}!0&amp;profile=newcustom-${opacdb}" % u)
    opacdb = get_hip_db(catdb)
    return urltemplate.substitute(bibno=bibno, opacdb=opacdb) 

def is_icos( catdb ):
    """
    Determines if this belongs in the ICOS or books catalog; returns
    boolean value
    """
    if catdb.startswith('aip'):
        return False
    else:
        return True

def get_bibno(record):
    """
    Gets bib number from record.
    
    Although getting the bib number from 999$a is more authoritative, we can't
    be sure that it'll be there as it requires the user to export the data
    from Horizon using MARCOUT. 998$b is inserted when using the "script"
    export profile, which everyone should be doing. 982$a is the least
    preferable as it's inserted manually. I changed the handling to return
    None instead of raising an exception because we can possibly anticipate
    code where getting the bib number isn't essential and returning None would
    be preferable.
    """
    if record['998'] is not None:
        if record['998']['b'] is not None:
            return record['998']['b']
    if record['999'] is not None:
        if record['999']['a'] is not None:
            return record['999']['a']
    if record['982'] is not None:
        if record['982']['a'] is not None:
            return record['982']['a']
    sys.stderr.write('Could not derive bib number from: %s' %
                    record['245'].format_field())
    return None

def get_catdb(record):
    """
    Gets catalog database from record.
    
    Is returning 'aipnbl' proper if it can't find 998$a? I'd guess so as the
    TypeErrors I'm seeing for NoneType seem to mostly becoming from serials
    records, which don't have item records like all other bib records should.
    They have "copy records" instead.
    """
    if record['998'] is not None:
        if record['998']['a'] is not None:
            return record['998']['a']
    return 'aipnbl'

def parse_date(record):
    """
    Gets date from record; used by docpres.py.
    
    Tries 245$f and $g first; if can't find those, it tries 260$c and then
    the 008. Should this return None instead of an empty string if it can't
    pullout a date? If so, code in docpres.py and ohilist.py will need to be
    adjusted.
    """
    datelist = []
    if record['245']['f'] or record['245']['g']:
        if record['245']['f']:
            datelist.append(record['245']['f'])
        if record['245']['g']:
            datelist.append(record['245']['g'])
        return ' '.join(datelist)
    if record['260']:
        if record['260']['c']:
            return record['260']['c']
    if record['008'].value()[7:11].isdigit():
        datelist.append(record['008'].value()[7:11])
        if record['008'].value()[11:15].isdigit():
            datelist.append(record['008'].value()[11:15])
        if len(datelist) > 1:
            return '-'.join(datelist)
        else:
            return ''.join(datelist)
    if get_bibno(record) is not None:
        sys.stderr.write('Could not derive date from bib number %s\n' %
                    get_bibno(record))
    else: 
        sys.stderr.write('Could not derive date or bib number from: %s\n' %
                    record['245'].format_field())
    return ''

def get_hip_db(catdb):
    """
    Sets OPAC database based upon catdb.
    
    This is a separate function from get_catdb() because one can anticipate
    possibly just wanting the catalog database and not the OPAC database for
    operations in the future.    
    """
    if is_icos(catdb):
        return 'icos'
    else:
        return 'aipnbl'

def strip_isbd(string):
    """
    Strips ISBD punctuation for normalization, etc.
    """
    return string.strip('.:,;/ ')
 
#
