# https://www.acmicpc.net/problem/17940

from sys import stdin
import heapq
input = stdin.readline

IMP = int(1e6)
INF = int(1e9)

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0))

    while q:
        cost, now = heapq.heappop(q)

        if cost > distance[now]:
            continue

        for i, nxt in enumerate(E[now]):
            if now == i:
                continue

            if nxt > 0:
                dist = cost + nxt
                if distance[i] > dist:
                    distance[i] = dist
                    heapq.heappush(q, (dist, i))


n, m = map(int, input().split())
C = [int(input()) for _ in range(n)]
E = [[-1] * n for _ in range(n)]
for i in range(n):
    con = list(map(int, input().split()))
    for j in range(len(con)):
        if con[j] == 0:
            E[i][j] = 0
        else:
            if C[i] == C[j]:
                E[i][j] = con[j]
            else:
                E[i][j] = con[j] + IMP

# print(E)
distance = [INF] * n
distance[0] = 0
dijkstra()
print(distance[m] // IMP, distance[m] % IMP)