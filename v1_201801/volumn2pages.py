import os

os.chdir('text_dw/')
for t in os.listdir(os.getcwd()):
	with open(t,'r') as fi:
		volumn = {}
		for l in fi:
			if l.startswith('----- ') and l.endswith(' -----\n'):
				page = l.split(' / ')[0][6:]
				volumn[page] = ''
			else:
				volumn[page] += l
		for k,v in volumn.items():
			with open('../pages/'+t.split('.txt')[0]+'_'+k+'.txt','w') as fo:
				fo.write(v)
