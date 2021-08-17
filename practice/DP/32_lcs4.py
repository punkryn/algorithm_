# https://www.acmicpc.net/problem/13711
# LIS

import bisect

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

order = [0] * 101010

for i in range(1, n + 1):
    order[b[i-1]] = i

a.insert(0, 0)
for i in range(1, n + 1):
    a[i] = order[a[i]]

print(a, order)

ans = 0
dp1 = [-1]
for i in range(1, n + 1):
    if dp1[-1] < a[i]:
        dp1.append(a[i])
        ans += 1
    else:
        dp1[bisect.bisect(dp1, a[i])] = a[i]

print(ans)