# https://www.acmicpc.net/contest/problem/658/2

from sys import stdin

n, m = map(int, input().split())

keyword = dict()
for _ in range(n):
    key = stdin.readline().strip()
    keyword[key] = 1
post = [list(stdin.readline().strip().split(',')) for _ in range(m)]

#print(keyword)
#print(post)
total = n
for p in post:
    for key in p:
        try:
            keyword[key] -= 1
            if keyword[key] == 0:
                total -= 1
        except(KeyError):
            continue

    print(total)