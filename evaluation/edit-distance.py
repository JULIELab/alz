def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)

    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]
    
def levenshtein-2(s, t):
        ''' From Wikipedia article; Iterative with two matrix rows. '''
        if s == t: return 0
        elif len(s) == 0: return len(t)
        elif len(t) == 0: return len(s)
        v0 = [None] * (len(t) + 1)
        v1 = [None] * (len(t) + 1)
        for i in range(len(v0)):
            v0[i] = i
        for i in range(len(s)):
            v1[0] = i + 1
            for j in range(len(t)):
                cost = 0 if s[i] == t[j] else 1
                v1[j + 1] = min(v1[j] + 1, v0[j + 1] + 1, v0[j] + cost)
            for j in range(len(v0)):
                v0[j] = v1[j]
                
        return v1[len(t)]

with open('Ground-Truth-1.txt', 'r') as f:
    s1=f.read()
with open('Ground-Truth-2.txt', 'r') as f:
    s2=f.read()

with open('textlist_page_1.txt','r') as f:
    for t in f:
        fn = t.rstrip()
        with open(fn,'r') as ft:
            st = ft.read()
            print(fn)
            print(levenshtein(s1, st))

with open('textlist_page_2.txt','r') as f:
    for t in f:
        fn = t.rstrip()
        with open(fn,'r') as ft:
            st = ft.read()
            print(fn)
            print(levenshtein(s2, st))
