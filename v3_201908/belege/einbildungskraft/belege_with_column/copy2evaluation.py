import os

folder = "sampling"

file_list = os.listdir(folder)

for f in file_list:
	if f in os.listdir("LA_20191122_korrigiert"):
		os.system("cp LA_20191122_korrigiert/"+f+" evaluation/"+f.split(".")[0]+"_la.txt")
		os.system("cp "+folder+"/"+f+" evaluation/"+f.split(".")[0]+"_td.txt")