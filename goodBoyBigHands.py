import re

fin = []
l = int(input())

for i in range(l):
    text = input().lower()
    fin += re.sub(r'[^\w\s]', '', text).split()

n = int(input())
for i in range(n):
    l = int(input())
    for i in range(l):
        text = input().lower()
        text = re.sub(r'[^\w\s]', '', text).split()
        temp = [x for x in text if x in fin]
        if len(temp) >= len(text) / 2:
            print("GOOD BOY!")
        else:
            print("BIG HANDS!")