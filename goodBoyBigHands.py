import re

fin = []
temp1 = []
l = int(input())
text = ''
for i in range(l):
    # for i in range(32, 127):
    #     text += chr(i)
    text = input().lower().split()
    for s in text:
        x = re.sub("[^a-zA-Z]","", s)
        if x != '':
            fin.append(x)

print(fin)

n = int(input())
for i in range(n):
    l = int(input())
    for i in range(l):
        temp1 = []
        text = input().lower().split()
        for s in text:
            x = re.sub("[^a-zA-Z]","", s)
            if x != '':
                temp1.append(x)

        print(temp1)
        temp = [x for x in temp1 if x in fin]
        print(temp)
        if len(temp) >= len(temp1) / 2:
            print("GOOD BOY!")
        else:
            print("BIG HANDS!")