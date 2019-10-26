import xml.etree.ElementTree as ET
import os
import re
import pandas as pd
from operator import itemgetter

search_term = re.compile(r'[Ee]inbildung[ſs]kr[äa]ft')

count_beleg = 0

context_n = 10

df_column = pd.read_csv("all_with_column.tsv",sep="\t",quoting=3,engine='python',dtype=str,encoding='utf-8')

os.chdir('../../xml_compiled/')
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
			page = elem_id.text
			inpage = []
			for elem_l in elem.findall("{http://www.tei-c.org/ns/1.0}content/{http://www.tei-c.org/ns/1.0}p"):
				ll = elem_l.text.strip()
				ll = ll.replace('&gt;','>')
				ll = ll.replace('&amp;','&')
				ll = ll.replace('&lt;','<')
				inpage.append(ll)
			num = len(inpage)
			connect = False
			for i in range(num):
				if not connect:
					to_search = inpage[i]
				else:
					to_search = inpage[i-1].rstrip('-')+inpage[i]
				if search_term.search(to_search):
					count_beleg += 1
					if connect:
						left = i-1
						right = i
					else:
						left = i
						right = i
					context_left = left - context_n
					if context_left < 0:
						context_left = 0
					context_right = right + context_n
					if context_right > num-1:
						context_right = num-1
					row = df_column.loc[(df_column['Volume'] == t.split(".")[0]) & (df_column['Page'] == elem_id.text) & (df_column['KWIC'] == to_search)]
					if len(row.index) > 0:
						with open("../belege/einbildungskraft/belege_with_column/all/"+t.split(".")[0]+"_"+elem_id.text+"_"+str(left)+".item","w",encoding="utf-8") as f:
							f.write(year)
							f.write("\n")
							f.write(vol)
							f.write("\n")
							f.write(page)
							f.write("\n")
							f.write(row.iloc[0]['Column'])
							f.write("\n")
							f.write(str(left+1))
							f.write("\n")
							f.write("\n")
							for line_n in range(context_left,left):
								f.write(inpage[line_n])
								f.write("\n")
							f.write("***\n")
							for line_n in range(left,right+1):
								f.write(inpage[line_n])
								f.write("\n")
							f.write("***\n")
							for line_n in range(right+1,context_right+1):
								f.write(inpage[line_n])
								f.write("\n")
							f.write('\n')
							f.write('\n')
							f.write(url)
							f.write('\n')
							f.write('\n')
							f.write('\n')
					else:
						with open("../belege/einbildungskraft/belege_rest.tsv","a",encoding="utf-8") as fo:
							fo.write(t.split(".")[0])
							fo.write("\t")
							fo.write(elem_id.text)
							fo.write("\t")
							fo.write(str(left+1))
							fo.write("\t")
							fo.write(to_search)
							fo.write("\t")
							fo.write(url)
							fo.write("\n")
				connect = False
				if inpage[i].endswith('Ein-') or inpage[i].endswith('ein-') or inpage[i].endswith('Einbilduns-') or inpage[i].endswith('Einbildungs') or inpage[i].endswith('einbildungſ') or inpage[i].endswith('einbildungſ-') or inpage[i].endswith('einbildungs') or inpage[i].endswith('einbildungs-') or inpage[i].endswith('Einbildungſ') or inpage[i].endswith('Einbildungſ-'):
					connect = True
print(count_beleg)