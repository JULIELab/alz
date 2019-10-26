import os
import sys
import pandas as pd

#df = pd.read_csv("../all_with_column.tsv",sep="\t",quoting=3,engine='python',dtype=str,encoding='utf-8')

#df.groupby('Column').count().to_csv("column_freq.tsv", sep='\t', encoding='utf-8')

os.system("mkdir temp")

os.chdir('all/')

for beleg in os.listdir(os.getcwd()):
	with open(beleg,"r", encoding="utf-8",errors='ignore') as f:
		content = f.readlines()
		#already processed: PHILOSOPHIE
		if content[3].strip() == "":
			os.system("cp "+beleg+" ../temp/")