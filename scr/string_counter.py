import os

os.chdir('pages/')
#s  = input("To be search: ")
dic = {}
pages = 0
total = 0
for t in os.listdir(os.getcwd()):
	volumn = t.split('_')[0]
	page = t.split('_')[1].split('.txt')[0]
	if not volumn in dic:
		dic[volumn] = {}
	file  = open(t, 'r').read()
	num = file.count('romant') + file.count('Romant')
	with open('../countlist.txt','a') as f:
		f.write(t)
		f.write('\t')
		f.write(str(num))
		f.write('\n')
	dic[volumn][page] = num
	if num > 0:
		pages += 1
		total += num
		print(t)
		print(num)
volumns = list(dic.items())
volumns.sort(key=lambda e: e[0], reverse=False)
#print(volumns)
for vol in volumns:
	v = vol[1]
	pp = list(v.items())
	pp.sort(key=lambda e: e[0], reverse=False)
	p_num = 0
	for p in pp:
		p_num += p[1]
	print(vol[0], p_num)
	#print(pp)
print('pages:',pages)
print('items:',total)
