# 4 2
# 1 1 1 1

# 11 5
# 1 2 3 4 2 5 3 1 1 2 5

# https://www.acmicpc.net/problem/2003

from sys import stdin

n, m = map(int, stdin.readline().split())

a = list(map(int, stdin.readline().split()))

low, high = 0, 0
count = 0
while high < n:
    s = sum(a[low: high+1])
    print(low, high, s)
    if s >= m:
        count += 1 if s == m else 0
        s -= a[low]
        low += 1
    else:
        s += a[high]
        high += 1
print(count)