# https://www.acmicpc.net/problem/1717

from sys import stdin
from sys import setrecursionlimit

setrecursionlimit(100000)

def find_parent(parent, r):
    if parent[r] != r:
        parent[r] = find_parent(parent, parent[r])
    return parent[r]

def union(parent, r1, r2):
    r1 = find_parent(parent, r1)
    r2 = find_parent(parent, r2)

    if r1 < r2:
        parent[r2] = r1
    else:
        parent[r1] = r2

n, m = map(int, stdin.readline().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, stdin.readline().split())

    if op == 0:
        union(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')