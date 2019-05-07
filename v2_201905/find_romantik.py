import xml.etree.ElementTree as ET
import os
import re
from operator import itemgetter

#romantik = re.compile(r'(Romant|[^a-zP]romant)')
romantik = re.compile(r'([Rr]omantiſ|[Rr]omant\.|[Rr]omantic|Romantik)')
#romantik = re.compile(r'Romantik')

ro = False
countyear = {}
m=0

os.chdir('xml_compiled/')
with open('../romantik.tsv','w') as f:
	treffer_list = []
	for t in os.listdir(os.getcwd()):
		tree = ET.parse(t)
		root = tree.getroot()
		for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}sourceDesc/{http://www.tei-c.org/ns/1.0}biblFull/{http://www.tei-c.org/ns/1.0}publicationStmt/{http://www.tei-c.org/ns/1.0}date/[@type='publication']"):
			year = elem.text
		for elem in root.findall("./{http://www.tei-c.org/ns/1.0}teiHeader/{http://www.tei-c.org/ns/1.0}fileDesc/{http://www.tei-c.org/ns/1.0}sourceDesc/{http://www.tei-c.org/ns/1.0}biblFull/{http://www.tei-c.org/ns/1.0}publicationStmt/{http://www.tei-c.org/ns/1.0}volume"):
			vol = elem.text
		for elem in root.findall("./{http://www.tei-c.org/ns/1.0}volume/{http://www.tei-c.org/ns/1.0}page"):
			for elem_ref in elem.findall("{http://www.tei-c.org/ns/1.0}ref"):
				url = elem_ref.text
			for elem_id in elem.findall("{http://www.tei-c.org/ns/1.0}id"):
				n = 0
				for elem_l in elem.findall("{http://www.tei-c.org/ns/1.0}content/{http://www.tei-c.org/ns/1.0}p"):
					n+=1
					ll = elem_l.text.strip()
					ll = ll.replace('&gt;','>')
					ll = ll.replace('&amp;','&')
					ll = ll.replace('&lt;','<')
					if ro:
						ll = lastline+ll
						lastline = ''
					if romantik.search(ll):
						treffer = [t,url,year,vol,elem_id.text,str(n),ll]
						treffer_list.append(treffer)
						if not year in countyear:
							countyear[year]=1
						else:
							countyear[year]+=1
						if ro:
							m+=1
						# f.write(t)
						# f.write('\n')
						# f.write(url)
						# f.write('\n')
						# f.write(year)
						# f.write('\t')
						# f.write(vol)
						# f.write('\n')
						# f.write(elem_id.text)
						# f.write('\t')
						# f.write(str(n))
						# f.write('\n')
						# f.write(ll)
						# f.write('\n')
						# f.write('\n')
					if ll.endswith('ro-') or ll.endswith('ro') or ll.endswith('Ro') or ll.endswith('Ro-') or ll.endswith('roman-') or ll.endswith('Roman-') or ll.endswith('roman') or ll.endswith('Roman'):
						ro = True
						lastline=ll.rstrip('-')
					else:
						ro = False
	treffer_list = sorted(treffer_list, key = itemgetter(2))
	for r in treffer_list:
		f.write(r[0])
		f.write('\n')
		f.write(r[1])
		f.write('\n')
		f.write(r[2])
		f.write('\t')
		f.write(r[3])
		f.write('\n')
		f.write(r[4])
		f.write('\t')
		f.write(r[5])
		f.write('\n')
		f.write(r[6])
		f.write('\n')
		f.write('\n')
print(countyear)
print(m)