# 1
# 2
# 0 0
# 0 100
# 1.0

import sys
import math

def find_parent(parent, r):
    if parent[r] != r:
        parent[r] = find_parent(parent, parent[r])
    return parent[r]

def union(parent, r1, r2):
    r1 = find_parent(parent, r1)
    r2 = find_parent(parent, r2)

    if r1 > r2:
        parent[r1] = r2
    else:
        parent[r2] = r1

#sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    parent = [i for i in range(N + 1)]
    graph = []
    for i in range(len(X) - 1):
        for j in range(1, len(X)):
            x1, y1 = X[i], Y[i]
            x2, y2 = X[j], Y[j]
            dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            graph.append([dist, i, j])

    graph.sort()
    #print(graph)

    total = 0
    for v in graph:
        cost, x, y, = v
        #print(x, y)
        if find_parent(parent, x) != find_parent(parent, y):
            total += ((cost ** 2) * E)
            union(parent, x, y)

    print("#" + str(test_case), round(total))

