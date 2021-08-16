# https://www.acmicpc.net/problem/5214

from collections import deque

n, k, m = map(int, input().split())

graph = [[] for _ in range(200020)]
start_station = []
for i in range(1, m + 1):
    ho = list(map(int, input().split()))
    for s in ho:
        if s == 1:
            start_station.append((i + n, 1))
        graph[s].append((i + n, 1))
        graph[i + n].append((s, 0))

q = deque()
visited = [0] * (n + m + 1)
visited[1] = 1
for start in start_station:
    a, b = start
    q.append([a, b, 0])

if n == 1:
    print(1)
else:
    ans = 1
    while q:
        now, w, cost = q.popleft()

        if now == n:
            ans += cost
            break

        for i in graph[now]:
            nxt, w_ = i
            if visited[nxt] == 0:
                visited[nxt] = 1
                q.append((nxt, w_, cost + w))

    if ans == 1:
        print(-1)
    else:
        print(ans)