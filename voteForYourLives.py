a = int(input())
ans=[]
for i in range(a):
    b = int(input())
    votes = [int(x) for x in input().split()]
    tally = []
    for i in range(b+1):
        tally.append(0)
    for i in votes:
        if i == 0 or i == -1:
            tally[0] += 1
        else:
            tally[i] += 1
    temp = max(tally)
    zero = 0
    results =[]

    if tally.index(temp) == 0:
        results.append(0)
        tally[0] = -1
    temp = max(tally)

    if temp != 0:
        results.append(tally.index(temp))
        tally[tally.index(temp)] = -1
        while temp  in tally:
            zero = 1
            results.append(tally.index(temp))
            tally[tally.index(temp)] = -1
        if zero == 1:
            results.append(0)
        results.sort()
    results = list(dict.fromkeys(results))
    ans.append(results)

for i in ans:
    for j in i:
        print(j,end=" ")
    print()