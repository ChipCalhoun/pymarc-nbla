"""
mirrorpages.py - mark a. matienzo
requires:
    pymarc.py: http://www.textualize.com/pymarc (or from python cheeseshop)
    aipmarc.py: local AIP marc handling code (should be included)
    mptemplates.py: templates for HTML output (should be included)

usage: mirrorpages.py <marcfile> [output path for zip file]
"""

from pymarc import MARCReader, marc8_to_unicode
#from pymarc import get_fields, subjects, format_field, author
from aipmarc import get_catdb, get_bibno, hip_url, is_icos
from mptemplates import htmltemplate, indextop
import sys
import os
import errno
import zipfile
cwd = os.getcwd()
filelist = []

def build_div(fields, divclass):
    divlist = [build_div_html(marc8_to_unicode(field.format_field()),
                                divclass) for field in fields]
    divs = "".join(divlist)
    return divs
    
def build_div_html(data, divclass):
    div = '<div class="%s">%s</div>\n' % (divclass, data)
    return div

def record_as_html(rec, bn, db, fn):
    creator = ''
    if rec.author():
        creator = marc8_to_unicode(rec.author())
    creatordiv = build_div_html(creator, 'creator')
    title = marc8_to_unicode(rec['245'].format_field())
    titlediv = build_div_html(title, 'title')
    scopecontent = build_div(rec.get_fields('520'),
                                'abstract scopecontent')
    bioghist = build_div(rec.get_fields('545'), 'description bioghist')
    subjdiv = build_div(rec.subjects(), 'subject')
    addedentries = build_div(rec.addedentries(), 'addedentry')
    repos = build_div(rec.location(), 'isLocatedAt repos')
#    db = get_catdb(rec)
#    bn = get_bibno(rec)
    recordbody = '\n%s%s%s%s%s%s%s%s' % (creatordiv, titlediv, scopecontent,
                                            bioghist, subjdiv, addedentries,
                                            repos, catalogdiv)
    recordbodydiv = build_div_html(recordbody, 'record')
    url = hip_url(bn, db)
    out = htmltemplate.substitute(creator=creator, title=title, url=url,
                                    jsurl=url.replace('&amp;', '&'),
                                    recordbody=recordbodydiv)

#def write_htmlfile(record, fn):
    try:
        outfile = open(fn, 'w')
    except:
        write_error(fn)
    outfile.write(out.encode("utf-8"))
    outfile.close()
    #return out

def set_path():
    path = os.path.join(cwd,'tempmirr')
    check_path(path)
    check_path(os.path.join(path, 'books'))
    check_path(os.path.join(path, 'icos'))
    return path

def set_page_path(db):
    if is_icos(db):
        path = "icos"
    else:
        path = "books"
    return path

def set_file_name(path, bn):
    filename = os.path.join('%s', '%s.html') % (path, bibno)
    return filename

def check_path(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception, e:
            code, st = e
            if code != errno.EEXIST:
                st = "Error creating directory '%s': %s" % (path, str(e))
                sys.exit(1)

def write_error(fn):
    print 'Error creating file'
    fn.close()
    sys.exit(1)

def build_index(fn):
    header = indextop.substitute(title='Catalog Index')
    try:
        fh = open(fn, 'w')
        fh.write(header)
        return fh
    except: write_error(fh)
    
def build_metaindex(iterator, base, temp, fh):
    indexfn = 'catalog_%s.html' % iterator
    sitemap.write('%s%s\n' % (base, indexfn))
    append_link(indexfn, fh)
    filelist.append(indexfn)
    return build_index(os.path.join(temp, indexfn))

def make_link(url, linktext):
    link = '<a href="%s">%s</a>' % (url, linktext)
    return link 

def append_link(rf, fh):
    link = make_link(rf, rf)
    try:
        fh.write(build_div_html(link, 'floater'))
    except:
        write_error(fh)

def close_htmlfile(fh):
    try:
        fh.write('</body>\n</html>')
        fh.close()
    except:
        write_error(fh)
    
def create_googlefile(temp):
    gindexfn = 'google37894732151ee500.html' 
    gindex = open(os.path.join(temp, gindexfn),'w')
    gindex.close()
    filelist.append(gindexfn)

def clean_tempdir(path):
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))
      
try:
    outpath = sys.argv[2]
    check_path(outpath)
except IndexError: 
    outpath = os.getcwd()

try:
    marcfile = sys.argv[1]
except IndexError:
    sys.exit('Usage: %s <marcfile> [outputdirectory]' % sys.argv[0])

outzip = zipfile.ZipFile(os.path.join(outpath,'catalog.zip'),
                            'w', zipfile.ZIP_DEFLATED)
reader = MARCReader(file(marcfile))
tempdirectory = set_path()
create_googlefile(tempdirectory)
indexiterator = 1
mainindexiterator = 1
baseurl = 'http://www.aip.org/history/catalog/'
sitemap = open(os.path.join(tempdirectory, 'sitemap.txt'), 'w')
mainindexfile = build_index(os.path.join(tempdirectory, 'catalog.html'))
mainindexurl = '%scatalog.html' % baseurl
sitemap.write(mainindexurl + '\n')
catalogdiv = build_div_html(make_link(mainindexurl, 'Catalog'),
                            'catalogOrIndex')
indexfile = build_metaindex(mainindexiterator, baseurl,
                            tempdirectory, mainindexfile)

for record in reader:
    catdb = get_catdb(record)
    bibno = get_bibno(record)
    pagepath = os.path.join(tempdirectory, set_page_path(catdb))
    serverpath = set_page_path(catdb)
    recordfn = set_file_name(pagepath, bibno)
    serverrecordfn = '%s/%s.html' % (serverpath, bibno)
    record_as_html(record, bibno, catdb, recordfn)
    sitemap.write('%s%s\n' % (baseurl, serverrecordfn))
    append_link(serverrecordfn, indexfile)
    filelist.append(serverrecordfn)
    if indexiterator % 2000 == 0:
        indexiterator = 0
        mainindexiterator += 1
        close_htmlfile(indexfile)
        indexfile = build_metaindex(mainindexiterator, baseurl,
                                    tempdirectory, mainindexfile)
    indexiterator += 1
close_htmlfile(indexfile)
close_htmlfile(mainindexfile)
sitemap.close()
filelist.extend(['sitemap.txt', 'catalog.html'])

os.chdir(tempdirectory) 
for file in filelist:
    outzip.write(file)
outzip.close()
os.chdir(cwd)
clean_tempdir(tempdirectory)
