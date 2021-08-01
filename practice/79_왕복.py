# 5 28
# 7 4 2 4 5

# https://www.acmicpc.net/problem/18311

n, k = map(int, input().split())
length = list(map(int, input().split()))

t_len = sum(length)

total = 0
if t_len > k:
    for i in range(n):
        total += length[i]
        if k < total:
            print(i + 1)
            break
else:
    k -= t_len
    #print(k)
    for i in range(n - 1, -1, -1):
        total += length[i]
        if k < total:
            print(i + 1)
            break