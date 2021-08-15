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
d = [0] * 200020
for i in range(1, l + 1):
    station = list(map(int, stdin.readline().split()))[:-1]
    for s in station:
        stations[i + n].append((s, 0))
        stations[s].append((i + n, 1))

for iii in range(13):
    print(stations[iii])

start, end = map(int, input().split())

INF = int(1e9) + 7

if start == end:
    print(0)
else:
    q = deque()
    q.append(start)
    for _ in range(1, n + l + 1):
        d[_] = INF
    d[start] = 0

    while q:
        # print(q)
        print(q, d[:15])
        cur = q.popleft()
        # print(now, cost)

        for p in stations[cur]:
            # print(p)
            nxt, w = p
            if d[nxt] <= d[cur] + 1:
                continue

            d[nxt] = d[cur] + w
            q.append(nxt)

    if d[end] == INF:
        ans = -1
    else:
        ans = d[end] - 1
    # print(d[:20])
    print(ans)

