import xml.etree.ElementTree as ET
import os
import re
from operator import itemgetter

#romantik = re.compile(r'(Romant|[^a-zP]romant)')
#romantik = re.compile(r'([Rr]omantiſ|[Rr]omant\.|[Rr]omantic|Romantik)')
romantik = re.compile(r'[Rr]omanti[ſs]ch')

ro = False
countyear = {}
m=0
line1 = ""
line2 = ""
line3 = ""
line4 = ""
line5 = ""

os.chdir('xml_compiled/')
filename = input("Output name:")
with open('../'+filename,'w',encoding="utf-8") as f:
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
				num = len(elem.findall("{http://www.tei-c.org/ns/1.0}content/{http://www.tei-c.org/ns/1.0}p"))
				for elem_l in elem.findall("{http://www.tei-c.org/ns/1.0}content/{http://www.tei-c.org/ns/1.0}p"):
					n+=1
					ll = elem_l.text.strip()
					ll = ll.replace('&gt;','>')
					ll = ll.replace('&amp;','&')
					ll = ll.replace('&lt;','<')
					line1 = line2
					line2 = line3
					line3 = line4
					line4 = line5
					line5 = ll
					output = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 + "\n" + line5
					if ro:
						if n + 1 == num:
							ll = lastline + line4
							lastline = ""
							output = line2 + "\n" + line3 + "\n" + line4 + "\n" + line5
						elif n == num:
							ll = lastline + line5
							output = line3 + "\n" + line4 + "\n" + line5
							lastline = ""
						else:
							ll = lastline + line3
							lastline = ""
					else:
						if n + 1 == num:
							ll = line4
							output = line2 + "\n" + line3 + "\n" + line4 + "\n" + line5
						elif n == num:
							ll = line5
							output = line3 + "\n" + line4 + "\n" + line5
						else:
							ll = line3
					if romantik.search(ll):
						if n+1 == num:
							n_l = n-1
						elif n == num:
							n_l = n
						else:
							n_l = n-2
						treffer = [t,url,year,vol,elem_id.text,str(n_l),output]
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
					if line3.endswith('ro-') or line3.endswith('ro') or line3.endswith('Ro') or line3.endswith('Ro-') or line3.endswith('roman-') or line3.endswith('Roman-') or line3.endswith('roman') or line3.endswith('Roman'):
						ro = True
						lastline = line3.rstrip('-')
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
