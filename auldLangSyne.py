a = int(input())
ans = []
for i in range(a):
    k = int(input())
    copyf = input().split()
    last = input().split()
    orig_index = len(copyf)
    last_num = copyf[-1]
    print(orig_index - (last.index(last_num) + 1))