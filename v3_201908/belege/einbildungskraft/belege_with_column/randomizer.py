import os
import random

folder = "LA_20191108"

file_list = os.listdir(folder)

sampling = random.sample(file_list, k=15)
print(len(sampling))

for f in sampling:
	os.system("cp "+folder+"/"+f+" sampling/")