'''
docpres.py - generates documentation preserved report
usage: docpres.py <marcfile> <newsletterissue> [--detailed]
newsletter issue should be in the format '07fall' (will find 'fa07fall'
automatically). '--detailed' option generates report with collection
summary & biographical statements. outputfilenames are 901a.html & 901b.html.

note 1: generates HTML in iso-8859-1; this is for easy windows compatibility,
so we can convert this to RTF for spencer without encoding problems. you'll
obviously lose some diacritics since it's not encoded in utf-8, but they're
usually not diacritics that we're concerned about. this is easily changed -
just change OUTPUT_ENCODING from 'iso-8859-1' to 'utf-8'. 
NOTE 1-CAC: Has been changed to UTF-8.

note 2: if the record is missing "required" fields (i.e. ICOS required fields
like 852, 901, 902, 904), the script might behave weird. MAKE SURE YOUR
RECORDS ARE CORRECT! :) seriously, it's better than debugging. i've tried to
insert code to make it handle missing fields, but it's not perfect. 
NOTE 2-CAC: This has led to erratic behavior. Attempting to debug.
'''

from pymarc import MARCReader, marc8_to_unicode
from aipmarc import strip_isbd, parse_date
from dptemplate import dppage
from itertools import groupby
from operator import itemgetter
import sys
import os

OUTPUT_ENCODING = 'utf-8'

def build_list(repos, colllist, detailed):
    colllist.append('''<div class="repository">
        <p class="reposname" style="color: maroon; font-weight: bold;">
        %s\n</p>''' % repos[0]['repos'].encode(OUTPUT_ENCODING, 'ignore'))
    for coll in repos:
        if coll['country'] == '':
            colllist.append('\n<span>RECORD MISSING 904 TAG</span>')
        colllist.append('\n<p class="coll"><b>%s</b> ' % 
                        coll['title'].encode(OUTPUT_ENCODING, 'ignore'))
        if coll['date'] != '':
            colllist.append('<b>Collection dates: %s</b> ' %
                        coll['date'].encode(OUTPUT_ENCODING, 'ignore'))
        if coll['extent'] != '':
            colllist.append('Size: %s ' %
                        coll['extent'].encode(OUTPUT_ENCODING, 'ignore'))
#        if coll['restrictions'] != '':
#            colllist.append('Restrictions: %s ' %
#                        coll['restrictions'].encode(OUTPUT_ENCODING, 'ignore'))
        if detailed == '--detailed':
            if coll['scopecontent'] != '':
                colllist.append('''\n<p>coll Summary: %s</p>''' %
                      coll['scopecontent'].encode(OUTPUT_ENCODING, 'ignore'))
            if coll['bioghist'] != '':
                colllist.append('\n<p>Biographical Statement: %s</p>' %
                        coll['bioghist'].encode(OUTPUT_ENCODING, 'ignore'))
        colllist.append('\n</p>')
    colllist.append('\n</div>')

def get_all_tag(rec, tag):
    """
    Should this return None if the tag isn't there? If so, adjust docpres.py
    """
    outlist = []
    for field in rec.get_fields(tag):
        outlist.append(field.format_field())
    return ' '.join(outlist)

def subfield_list(field, subfield_indicator):
#    subfields = field.get_subfields(subfield_indicator)
#    if subfields is not None:
#        return [subfield for subfield in subfields]
#    else:
#        return []
    out = []
    for i in subfield_indicator:
        sf = field.get_subfields(i)
        if sf is not None:
            out.extend([x for x in sf])
    return ' '.join(out)

def main(marcfile, newsletterissue, detailed):
    faissue = 'fa%s' % (newsletterissue)
    recordcounter = 0
    docpreslist = []
    try:
      detailed = sys.argv[3]
    except IndexError:
      detailed = ''
    reader = MARCReader(file(marcfile))
    for record in reader:
        """ 
        the try/except is a default handler so if exceptions come up the whole
        thing won't crash. better a slightly incomplete docpres list than no
        docpres list at all, right?
        
        use 'print get_bibno(record)' at different points to help debug.
        """
        try:
            # test to see if 901 tag is there
            if record['901'] is not None:
                if newsletterissue in record['901'].format_field():
                    """
                    this is not ideal, but we need to handle missing fields or
                    it'll skip entire records. perhaps add this as function to
                    aipmarc.py? EDIT - 3/7/08 - gsf working on adding fix to
                    pymarc for this.
                    """
                    if record['904'] is not None:
                        country = record['904']['a']
                    else: 
                        country = 'RECORD MISSING 904 TAG'
                    if record['852'] is not None:
                        repos = record['852'].format_field()
                    else:
                        repos = 'RECORD MISSING 852 TAG'
                    if record.author() is not None:
                        creator = record.author()
                    else: 
                        creator = 'RECORD MISSING AUTHOR'
                    title = subfield_list(record['245'],'akhbcnps')
                    title = '%s.' % strip_isbd(title)
    		#print marc8_to_unicode(title)
                    date = parse_date(record)
                    extent = get_all_tag(record, '300')
                    restrictions = get_all_tag(record, '506')
                    scopecontent = get_all_tag(record, '520')
                    bioghist = get_all_tag(record, '545')
                    item = {
                        'issue': record['901'].format_field(),
                        'country': country,
                        'repos': marc8_to_unicode(repos),
                        'creator': marc8_to_unicode(creator),
                        'title': marc8_to_unicode(title),
                        'date': date,
                        'extent': extent,
                        'restrictions': marc8_to_unicode(restrictions),
                        'scopecontent': marc8_to_unicode(scopecontent),
                        'bioghist': marc8_to_unicode(bioghist)
                     }
    		#print item
                    docpreslist.append(item)
                    recordcounter += 1
        except:
            pass
    
    print '%s records matching "%s" found.' % (recordcounter, newsletterissue)
    docpreslist.sort(key = lambda a :
                        (a['country'], a['repos'], a['creator'], a['title']))
    reposlist = [list(repos) for key, repos
                    in groupby(docpreslist,itemgetter('repos'))]
    newcoll = []
    newfa = []
    newcollsout = open('901a.html', 'w')
    newfasout = open('901b.html', 'w')
    
    for repos in reposlist:
        if faissue in repos[0]['issue']:
            build_list(repos, newfa, detailed)
        else:
            build_list(repos, newcoll, detailed)
    newcolls = ''.join(newcoll)
    newfas = ''.join(newfa)
    newcollsout.write(dppage.substitute(collections=newcolls,
                                        subtitle='New Collections'))
    newfasout.write(dppage.substitute(collections=newfas,
                                        subtitle='New Finding Aids'))
    newcollsout.close()
    newfasout.close()
    
if __name__ == "__main__":
    try:
      detopt = sys.argv[3]
    except IndexError:
      detopt = ''
    try:
      mf = sys.argv[1]
      issue = sys.argv[2]
      sys.exit(main(mf, issue, detopt))
    except IndexError:
      sys.exit('Usage: %s <marcfile> <issue> [--detailed]' % sys.argv[0])
