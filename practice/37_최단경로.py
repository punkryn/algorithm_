# 5 6
# 1
# 5 1 1
# 1 2 2
# 1 3 3
# 2 3 4
# 2 4 5
# 3 4 6

# https://www.acmicpc.net/problem/1753

from sys import stdin
import heapq

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append([b, c])

distance = [int(1e9)] * (v + 1)
#print(v, e)
q = []
distance[k] = 0
heapq.heappush(q, (0, k))

while q:
    dist, now = heapq.heappop(q)
    #print(distance)
    if distance[now] < dist:
        continue

    for item in graph[now]:
        cost = dist + item[1]
        if cost < distance[item[0]]:
            distance[item[0]] = cost
            heapq.heappush(q, (cost, item[0]))

for dis in distance[1:]:
    if dis == int(1e9):
        print('INF')
    else:
        print(dis)