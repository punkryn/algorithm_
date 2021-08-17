# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5

# https://www.acmicpc.net/problem/1920

def bs(a, target):
    low = 0
    high = len(a) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if a[mid] > target:
            high = mid - 1
        elif a[mid] < target:
            low = mid + 1
        else:
            break
    return mid

from sys import stdin
import bisect

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
x = list(map(int, stdin.readline().split()))

a.sort()

for j in x:
    if a[bisect.bisect(a, j) - 1] == j:
        print(bisect.bisect(a, j))
        print(1)
    else:
        print(0)

