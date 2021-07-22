# https://www.acmicpc.net/problem/1647

def find_parent(r1):
    if parent[r1] != r1:
        parent[r1] = find_parent(parent[r1])
    return parent[r1]

def union(r1, r2):
    r1 = find_parent(r1)
    r2 = find_parent(r2)

    if r1 > r2:
        parent[r1] = r2
    else:
        parent[r2] = r1

from sys import stdin

n, m = map(int ,input().split())

edges = []
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    edges.append([c, a, b])

parent = [i for i in range(n + 1)]
edges.sort()
maxvalue = 0
answer = 0
for edge in edges:
    c, a, b = edge
    if find_parent(a) != find_parent(b):
        if maxvalue < c:
            maxvalue = c
        answer += c
        union(a, b)

answer -= maxvalue
print(answer)