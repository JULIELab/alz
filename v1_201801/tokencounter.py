import nltk
import sys
import os

os.chdir(sys.argv[1])
n = 0
for t in os.listdir(os.getcwd()):
    with open(t,'r') as f:
        print(t)
        tokens = nltk.word_tokenize(f.read(), language='german')
        n += len(tokens)
print(n)
