import xml.etree.ElementTree as ET
import os
import re
from operator import itemgetter

romantik = re.compile(r'[Rr]omantic')

countyear = {}
context_n = 5

os.chdir('../../xml_compiled/')
treffer_list = []
for t in os.listdir(os.getcwd()):
	if t.startswith("bsb"):
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
				window = []
				n = 0
				num = len(elem.findall("{http://www.tei-c.org/ns/1.0}content/{http://www.tei-c.org/ns/1.0}p"))
				for elem_l in elem.findall("{http://www.tei-c.org/ns/1.0}content/{http://www.tei-c.org/ns/1.0}p"):
					n+=1
					ll = elem_l.text.strip()
					ll = ll.replace('&gt;','>')
					ll = ll.replace('&amp;','&')
					ll = ll.replace('&lt;','<')
					lastline = ""
					ro = False
					if n <= context_n*2+1:
						window.append(ll)
						if n == 1:
							continue
						middle = int((len(window)-1)/2)
						if n > 2:
							lastline = window[middle-1]
					elif n+context_n>num:
						if len(window) % 2 == 1:
							window = window[1:]
							continue
						elif len(window) == 2:
							lastline = window[0]
							window = window[1:]
							middle = -int((len(window)+1)/2)
						else:
							window = window[1:]
							middle = -int((len(window)+1)/2)
							lastline = window[middle-1]
					else:
						window = window[1:]
						window.append(ll)
						middle = int((len(window)-1)/2)
						lastline = window[middle-1]
					if lastline.endswith('ro-') or lastline.endswith('ro') or lastline.endswith('Ro') or lastline.endswith('Ro-') or lastline.endswith('roman-') or lastline.endswith('Roman-') or lastline.endswith('roman') or lastline.endswith('Roman') or lastline.endswith('Romanti-') or lastline.endswith('Romanti'):
						ro = True
						lastline = lastline.rstrip('-')
					else:
						ro = False
					to_search = window[middle]
					if ro:
						to_search = lastline+to_search
					if romantik.search(to_search):
						treffer = [t,url,year,vol,elem_id.text,str(n-abs(middle)),'\n'.join(window)]
						with open("../belege/romantic/bsb/"+t.split(".")[0]+"_"+elem_id.text+"_"+str(n-abs(middle))+".item","w",encoding="utf-8") as ff:
							ff.write(treffer[6])
							ff.write('\n')
							ff.write('\n')
							ff.write(treffer[1].split("presentation")[0]+"image/v2/"+t.split(".")[0]+"_"+elem_id.text+"/full/full/0/default.jpg")
							ff.write('\n')
							ff.write('\n')
							ff.write(treffer[5])
							ff.write('\n')