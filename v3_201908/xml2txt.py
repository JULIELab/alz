import xml.etree.ElementTree as ET
import os

os.chdir('xml_compiled')
for t in os.listdir(os.getcwd()):
	print(t)
	with open('../txt_compiled/'+t.split('.')[0]+'.txt','w') as f:
		f.write('year')
		f.write('\t')
		f.write('vol')
		f.write('\t')
		f.write('page')
		f.write('\t')
		f.write('line')
		f.write('\t')
		f.write('content')
		f.write('\n')
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
				p = elem_id.text
				n = 0
				for elem_l in elem.findall("{http://www.tei-c.org/ns/1.0}content/{http://www.tei-c.org/ns/1.0}p"):
					n+=1
					ll = elem_l.text.strip()
					ll = ll.replace('&gt;','>')
					ll = ll.replace('&amp;','&')
					ll = ll.replace('&lt;','<')
					f.write(year)
					f.write('\t')
					f.write(vol)
					f.write('\t')
					f.write(str(p))
					f.write('\t')
					f.write(str(n))
					f.write('\t')
					f.write(ll)
					f.write('\n')