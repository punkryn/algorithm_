# 4 3
# 1 3 -1
# 2 3 -1
# 2 3 4 -1
# 1 3

# https://www.acmicpc.net/problem/2021

from collections import deque
from sys import stdin

n, l = map(int, input().split())

stations = [[] for _ in range(n + 1 + n + 1)]
for i in range(1, l + 1):
    station = list(map(int, stdin.readline().split()))[:-1]
    for s in station:
        stations[i + n].append(s)
        stations[s].append(i + n)

# print(stations[:11], stations[100000: 100011])

start, end = map(int, input().split())

# print(graph)

# print(stations)

q = deque()
q.append((start + n, 0))
visited = [0] * (n + 1)
visited[start] = 1

if end in stations[start + n]:
    ans = 0
    q.popleft()
else:
    ans = -1
while q:
    # print(q)
    now, cost = q.popleft()
    # print(now, cost)

    if now - n == end:
        ans = cost
        break
    # print(now)
    for p in stations[now]:
        # print(p)
        if visited[p] == 0:
            visited[p] = 1
            q.append((p + n, cost + 1))


# print(distance)
print(ans)