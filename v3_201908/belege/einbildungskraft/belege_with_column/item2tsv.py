import os

os.chdir('bisher_korrigiert/')
with open("../bisher.tsv","w", encoding="utf-8") as fo:
	for beleg in os.listdir(os.getcwd()):
		with open(beleg,"r", encoding="utf-8") as f:
			flag = False
			ifbind = False
			sentence = ""
			content = f.readlines()
			fo.write(beleg.split('.')[0])
			fo.write('\t')
			fo.write(content[0].strip())
			fo.write('\t')
			fo.write(content[1].strip())
			fo.write('\t')
			fo.write(content[2].strip())
			fo.write('\t')
			fo.write(content[3].strip())
			fo.write('\t')
			fo.write(content[4].strip())
			fo.write('\t')
			for l in content:
				if flag:
					if ifbind:
						sentence += l.strip().rstrip("-")
					else:
						sentence += ' '+l.strip().rstrip("-")
					if l.strip().endswith('-'):
						ifbind = True
					else:
						ifbind = False
				if l.startswith("https"):
					flag = True
					fo.write(l.strip())
					fo.write('\t')
			fo.write(sentence.strip())
			fo.write('\n')