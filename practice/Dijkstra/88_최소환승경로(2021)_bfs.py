# 4 3
# 1 3 -1
# 2 3 -1
# 2 3 4 -1
# 1 3

# https://www.acmicpc.net/problem/2021

from collections import deque
from sys import stdin

n, l = map(int, input().split())

stations = [[] for _ in range(200020)]

for i in range(1, l + 1):
    station = list(map(int, stdin.readline().split()))[:-1]
    for s in station:
        stations[i + n].append((s, 0))
        stations[s].append((i + n, 1))

start, end = map(int, input().split())

if start == end:
    print(0)
else:
    q = deque()
    q.append((start, 0))

    visited = [0] * (n + l + 1)
    visited[start] = 1
    ans = 0
    flag = False
    while q:
        now, cost = q.popleft()

        if now == end:
            ans = cost
            flag = True
            break

        for station in stations[now]:
            nxt, w = station
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append((nxt, cost + w))

    if flag:
        print(ans-1)
    else:
        print(-1)

