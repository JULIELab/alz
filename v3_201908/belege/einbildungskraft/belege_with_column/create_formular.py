import os
import random
import pandas as pd

df = pd.read_csv('bisher.tsv',sep='\t',encoding="utf-8",names=['year','volume','page','column','line','url','sentence'])

newdf = df.sample(n=1)

with open('google_script.txt','w',encoding='utf-8') as f:
	f.write('function createForm() {\n')
	f.write('\titem = \"')
	f.write('Einbildungskraft in der ALZ\";\n')
	f.write('\tvar form = FormApp.create(item)\n')
	f.write('\t\t.setTitle(item)\n')
	f.write('\t\t.setDescription(\"Anleitungen\")\n')
	f.write('\n')
	f.write('\tquestion1 = \"Ist das Wort \\"Einbildungskraft\\" hier positiv oder negativ verwendet? Wenn Sie nicht entscheiden, wählen Sie bitte \\"unentschieden\\".\";\n')
	f.write('\n')
	for index,row in newdf.iterrows():
		f.write('\tvar classSection = form.addPageBreakItem()\n')
		f.write('\t\t.setTitle(\"')
		f.write(row['sentence'].replace('\"','\\"'))
		f.write('\")\n')
		f.write('\titem = question1;\n')
		f.write('\tvar choices = [\"Positiv\", \"Negativ\", \"unentschieden\"];\n')
		f.write('\tform.addMultipleChoiceItem()\n')
		f.write('\t\t.setTitle(question1)\n')
		f.write('\t\t.setChoiceValues(choices)\n')
		f.write('\t\t.setRequired(true);\n')
		f.write('\n')
	f.write('}')
