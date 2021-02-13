import math

stars = []
teles = []
s, t = map(int, input().split())
print(s, t)

for i in range(s):
    x2, y2, z2, b = map(int, input().split())
    d = math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)
    a = b / d ** 2
    stars.append([x2, y2, z2, a])

print(stars)

for i in range(t):
    count = 0
    tele = int(input())
    


