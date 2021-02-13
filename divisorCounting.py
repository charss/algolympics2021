import math

a = int(input())
memo = {}
check = 0
def count_factors(n):
    return len(set(x for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0 for x in (i, n // i)))

for i in range(a):
    arr = []
    n, m = map(int, input().split())
    temp = count_factors(n)
    i = 0
    while i != m:
        n += 1
        
        if n in memo:
            check = memo[n]
        else:
            memo[n] = count_factors(n)
            check = memo[n]

        if check <= temp:
            i += 1
    
    print(n)
