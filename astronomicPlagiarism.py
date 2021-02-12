import re
x = int(input())

found = False
toto = input()
arr = re.split(r'(\s+)', toto)
toto = [sorted(j) for j in arr]
papers = []

for i in range(x):
    work = input()
    arr = re.split(r'(\s+)', work)
    work = [sorted(j) for j in arr]
    
    if work == toto:
        print(i + 1)
        found = True
    
if found is False: print('INNOVATIVE WORK')


