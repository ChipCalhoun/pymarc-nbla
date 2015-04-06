'''
ohilist.py - generates oral history interview list for webpage 
usage: ohilist.py <marcfile>
output: "index.html" and "transcripts.html" in the current directory
'''

from aipmarc import get_catdb, get_bibno, parse_date
from ohitemplate import ohipage
from pymarc import MARCReader, marc8_to_unicode
from time import strftime
from umlautsort import alafiling
import urllib2
import sys
import os
import string

def make_link(url, linktext):
    link = '<a href="%s">%s</a>' % (url, linktext)
    return link
    
def make_page(ohidict, fn, title, backlink):
    date = strftime('%B %d' + ', ' + '%Y')
    listbody = ['<div id="ohiList-nav" class="listNav"></div><ul id="ohiList">']
    ohikeys = ohidict.keys()
    ohikeys.sort()

    for key in ohikeys:
        linklist = [link for link in ohidict[key]]
        listbody.extend(linklist)
    listbody.append('</ul>\n')
	
    body = "".join(listbody)
    fh = open(fn,'w')
    fh.write(ohipage.substitute(date=date, title=title,
                                body=body, backlink=backlink).encode("utf-8"))
    fh.close()
    
def main(marcfile):
    reader = MARCReader(file(marcfile))
    letters = list(string.uppercase)
    interviews = []
    ohiindex = {}
    ohititle = 'Oral History Interviews held by the Niels Bohr Library'
    transtitle = 'Online Oral History Transcripts from the Niels Bohr Library'
    ohibacklink = """A <a href="http://aip.org/history/ohilist/transcripts.html">separate list of transcripts available online</a> is also available."""
    transbacklink = """A <a href="http://aip.org/history/ohilist/">separate list of all transcripts</a> is also available."""
    transindex = {}
    recordcounter = 0

    for record in reader:
        if record['998'] is not None:
			collection = record.get_fields('998')
			for field in collection:
				collectionC = field['c']
				if collectionC == 'oh':
					catdb = get_catdb(record)
					bibno = get_bibno(record)
					transcript_url = None
					if record['856'] is not None:
						links = record.get_fields('856')
						for field in links:
							if 'http://www.aip.org/history/ohilist' in field['u']:
								transcript_url = field['u']
					url = 'http://www.aip.org/history/catalog/%s/%s.html' % (catdb,
																		 bibno)
					interviewee = marc8_to_unicode(record.author())
					date = parse_date(record)
					interviewdate = '(Interview date: %s)' % date.rstrip(',. ')
					interview = [interviewee, interviewdate]
					label = " ".join(interview)
					interviews.append((url, label, transcript_url, alafiling(label)))
					recordcounter += 1
				else:
					pass

    status = '%d OHI records found in %s' % (recordcounter, marcfile)

    if recordcounter == 0:
        sys.exit(status)
    else:
        sys.stderr.write(status)
        sys.stderr.write('\n')

    interviews.sort(key = lambda interviewkey: interviewkey[3])

    for interview in interviews:
        for letter in letters:
            initial = interview[1].upper()[0]
            if initial == letter:
                linkdata = '<li>%s' % make_link(interview[0], interview[1])
                if interview[2] is not None:
                    try:
                        urllib2.urlopen(interview[2])
                    except urllib2.HTTPError, e:
                        if e.code == 404:
                            sys.stderr.write('404 on %s\n' % interview[2])
                        else:
                            sys.stderr.write('Fail: %d, %s' % (e.code, e.msg))
                    except urllib2.URLError, e:
                        sys.stderr.write('Fail: %s' % e.reason)
                    linkdata = "%s - <strong>%s</strong>" % (linkdata,
                        make_link(interview[2],
                        'Online transcript available'))
                    transonlydata = '<li>%s</li>\n' % make_link(interview[2],
                                                           interview[1])
                    transindex.setdefault(letter,[]).append(transonlydata)
                linkdata = '%s</li>\n' % linkdata
                ohiindex.setdefault(letter,[]).append(linkdata)

    make_page(ohiindex, 'index.html', ohititle, ohibacklink)
    if transindex != {}:
        make_page(transindex, 'transcripts.html', transtitle, transbacklink)
    
if __name__ == '__main__':
    try:
      mf = sys.argv[1]
      sys.exit(main(mf))
    except IndexError:
      sys.exit('Usage: %s <marcfile>' % sys.argv[0])