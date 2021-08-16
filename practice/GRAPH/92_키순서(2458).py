# https://www.acmicpc.net/problem/2458

from sys import stdin
input = stdin.readline

from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
matrix = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    matrix[a][b] = 1

for i in range(1, n + 1):
     for j in range(1, n + 1):
         for k in range(1, n + 1):
             if j == k: continue
             if matrix[j][i] and matrix[i][k]:
                matrix[j][k] = 1

ans = 0
for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if i == j: continue
        if matrix[i][j] == 0 and matrix[j][i] == 0:
            cnt += 1

    if cnt == 0:
        ans += 1

print(ans)