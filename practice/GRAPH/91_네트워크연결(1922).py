# https://www.acmicpc.net/problem/1922

from sys import stdin
input = stdin.readline

def find_parent(r):
    if parent[r] != r:
        parent[r] = find_parent(parent[r])
    return parent[r]

def union(r1, r2):
    r1 = find_parent(r1)
    r2 = find_parent(r2)

    if r1 < r2:
        parent[r2] = r1
    else:
        parent[r1] = r2

n = int(input())
m = int(input())
graph = []

for _ in range(m):
    a, b, c = map(int, input().split())
    if a != b:
        graph.append((c, a, b))

parent = [i for i in range(n + 1)]
graph.sort()

total = 0
for edge in graph:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union(a, b)
        total += cost

print(total)