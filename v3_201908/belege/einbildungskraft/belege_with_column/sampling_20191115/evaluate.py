import os

file_list=os.listdir()

for f in file_list:
	if f.endswith("_td.txt"):
		prefix = f.split("_td")[0]
		os.system("dinglehopper "+f+" "+prefix+"_la.txt "+prefix)