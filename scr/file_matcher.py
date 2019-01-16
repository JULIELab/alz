with open("file_list.tsv",'r') as f:
	key = {}
	for l in f:
		pair = l.split('\t')
		key[pair[0].split('.txt')[0]] = pair[1].rstrip()

with open('verification/selected_all.txt','r') as fi, open('matched.tsv','w') as fo:
	for l in fi:
		fo.write(l.rstrip())
		fo.write('\t')
		fo.write(l.split('_')[0])
		fo.write('\t')
		fo.write(key[l.split('_')[0]])
		fo.write('\n')