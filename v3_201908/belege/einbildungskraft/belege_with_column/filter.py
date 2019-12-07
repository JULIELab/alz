import os
import sys
import pandas as pd

#df = pd.read_csv("../all_with_column.tsv",sep="\t",quoting=3,engine='python',dtype=str,encoding='utf-8')

#df.groupby('Column').count().to_csv("column_freq.tsv", sep='\t', encoding='utf-8')

os.system("mkdir 06_ANDERE")

os.chdir('all/')

for beleg in os.listdir(os.getcwd()):
	with open(beleg,"r", encoding="utf-8",errors='ignore') as f:
		content = f.readlines()
		#already processed: PHILOSOPHIE, SCHÖNE KÜNSTE, GESCHICHTE, ARZNEYGELAHRTHEIT, ERBAUUNGSSCHRIFTEN
		if content[3].strip() not in ['PHILOSOPHIE','SCHÖNE KÜNSTE','ARZNEYGELAHRTHEIT','GESCHICHTE','ERBAUUNGSSCHRIFTEN','VERMISCHTE SCHRIFTEN','LITERARISCHE ANZEIGEN','LITERARISCHE NACHRICHTEN','KLEINE SCHRIFTEN','I. Ankündigung neuer Bücher','INTELLIGENZ DES BUCH- UND KUNSTHANDELS','Ankündigungen neuer Bücher','DEUTSCHLANDSJOURNALENLITERATUR']:
			os.system("cp "+beleg+" ../06_ANDERE/")
			print(content[3].strip())