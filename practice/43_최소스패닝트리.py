# 3 3
# 1 2 1
# 2 3 2
# 1 3 3

# https://www.acmicpc.net/problem/1197

from sys import stdin

def find_parent(vertex, v):
    if vertex[v] != v:
        vertex[v] = find_parent(vertex, vertex[v])
    return vertex[v]

def union(vertex, v1, v2):
    v1 = find_parent(vertex, v1)
    v2 = find_parent(vertex, v2)

    if v1 != v2:
        vertex[v2] = v1

v, e = map(int, stdin.readline().split())
graph = []
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph.append([c, a, b])

graph.sort()

vertex = [i for i in range(v + 1)]

weight = 0
for item in graph:
    cost, v1, v2 = item
    if find_parent(vertex, v1) != find_parent(vertex, v2):
        weight += cost
        union(vertex, v1, v2)
print(weight)