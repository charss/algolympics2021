import re
c = int(input())

for i in range(c):
    word = input()
    arr = re.split(r'(\s+)', word)
    for x in range(len(arr)):
        if re.findall(r'[A-Z]', arr[x]):
            arr[x] = arr[x].upper()
    print(''.join(arr))