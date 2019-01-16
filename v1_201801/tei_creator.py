import os
import sys
import nltk
from datetime import datetime

def make_tei(idno,meta):
	if idno.startswith('bsb'):
		licence='<licence target="https://creativecommons.org/licenses/by-nc-sa/4.0/">\n<p>Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)</p>'
		link="https://app.digitale-sammlungen.de/bookshelf/"+idno
	else:
		link="https://archive.org/details/"+idno
		if idno.startswith('bub'):
			licence='<licence target="https://creativecommons.org/publicdomain/mark/1.0/">\n<p>Public Domain Mark 1.0</p>'
		else:
			licence="<licence>\n<p>NOT_IN_COPYRIGHT</p>"
	os.chdir(idno)
	print(os.getcwd())
	FileList=os.listdir()
	NFiles = len(FileList)
	NTokens = 0
	time=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	Ptok = {}
	for page in FileList:
		with open(page,'r') as f:
			tokens = nltk.word_tokenize(f.read(), language='german')
			Ptok[page] = len(tokens)
			NTokens += len(tokens)
	with open('../'+idno+'.xml','w') as f:
		f.write('<?xml version="1.0" encoding="UTF-8"?>\n<TEI xmlns="http://www.tei-c.org/ns/1.0">\n<teiHeader>\n<fileDesc>\n<titleStmt>\n<title>Allgemeine Literatur-Zeitung</title>\n<editor>\n<persName ref="https://orcidno.org/0000-0002-3324-0938">\n<surname>Duan</surname>\n<forename>Tinghui</forename>\n</persName>\n</editor>\n<editor>\n<persName ref="">\n<surname>Hahn</surname>\n<forename>Udo</forename>\n</persName>\n</editor>\n<respStmt>\n<orgName ref="https://www.julielab.de">JULIE Lab</orgName>\n</respStmt>\n</titleStmt>\n<editionStmt>\n<edition>Version 1.0</edition>\n<ocr>')
		f.write(meta[idno]['ocr'])
		f.write('</ocr>\n</editionStmt>\n<extent>\n<measure type="images">')
		f.write(str(NFiles))
		f.write('</measure>\n<measure type="tokens">')
		f.write(str(NTokens))
		f.write('</measure>\n</extent>\n<publicationStmt>\n<publisher>\n<orgName role="project">JULIE Lab</orgName>\n<address>\n<addrLine>Fürstengraben 27, 07743 Jena</addrLine>\n<country>Germany</country>\n</address>\n</publisher>\n<pubPlace>Jena</pubPlace>\n<date type="publication">')
		f.write(time)
		f.write('</date>\n<availability>\n')
		f.write(licence)
		f.write('\n</licence>\n</availability>\n<idno>\n<idno type="URLWeb">https://raw.githubusercontent.com/JULIELab/alz/master/v1_201801/xml/')
		f.write(idno)
		f.write('.xml</idno>\n<idno type="DTADirName">')
		f.write(idno)
		f.write('</idno>\n</idno>\n</publicationStmt>\n<sourceDesc>\n<biblFull>\n<titleStmt>\n<title>Allgemeine Literatur-Zeitung</title>\n</titleStmt>\n<publicationStmt>\n<pubPlace></pubPlace>\n<date type="publication">')
		f.write(meta[idno]['year'])
		f.write('</date>\n<volume>')
		f.write(meta[idno]['vol'])
		f.write('</volume>\n</publicationStmt>\n</biblFull>\n<msDesc>\n<msIdentifier>\n<repository>')
		f.write(meta[idno]['contributor'])
		f.write('</repository>\n<idno>\n<idno type="URLCatalogue">')
		f.write(link)
		f.write('</idno>\n</idno>\n</msIdentifier>\n</msDesc>\n</sourceDesc>\n</fileDesc>\n<profileDesc>\n<langUsage>\n<language ident="deu">German</language>\n</langUsage>\n</profileDesc>\n</teiHeader>\n\n')
		
		f.write('<volume>\n')
		for page in FileList:
			f.write('\t<page>\n')
			f.write('\t\t<id>')
			f.write(page.split('.')[0].split('_')[-1])
			f.write('</id>\n')
			f.write('\t\t<ref>')
			if idno.startswith('bsb'):
				f.write('https://api.digitale-sammlungen.de/iiif/presentation/v2/'+idno+'/canvas/'+page.split('.')[0].split('_')[-1].lstrip('0')+'/view')
			else:
				f.write('https://archive.org/details/'+idno+'/page/n'+page.split('.')[0].split('_')[-1].lstrip('0'))
			f.write('</ref>\n')
			f.write('\t\t<tok>')
			f.write(str(Ptok[page]))
			f.write('</tok>\n')
			f.write('\t\t<content>\n')
			with open(page,'r') as fi:
				for l in fi:
					ll = l.strip()
					if ll!='':
						ll = ll.replace('&','&amp;')
						ll = ll.replace('<','&lt;')
						ll = ll.replace('>','&gt;')
						f.write('\t\t\t<p>')
						f.write(ll)
						f.write('</p>\n')
			f.write('\t\t</content>\n')
			f.write('\t</page>\n')
		f.write('</volume>\n')
		f.write('</TEI>\n')
	os.chdir('..')
	print(os.getcwd())

meta={}
with open(sys.argv[1],'r') as f:
	for l in f:
		info=l.rstrip().split('\t')
		meta[info[0]]={'year':info[1],'vol':info[2],'contributor':info[3],'ocr':info[4]}

for k in meta:
	make_tei(k,meta)
