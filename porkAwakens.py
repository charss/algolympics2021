n = int(input())
b = int(input())
g = input().split()
p = input().split()

g = [int(x) for x in g]
p = [int(x) for x in p]
tot = 0
for x, y in zip(g, p):
    tot += x * y

print(b // tot)