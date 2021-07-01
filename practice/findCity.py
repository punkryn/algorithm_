# https://www.acmicpc.net/problem/18352

# 4 4 2 1
# 1 2
# 1 3
# 2 3
# 2 4

from collections import deque
from sys import stdin

n, m, k, x = map(int, stdin.readline().split())
roads = []
for _ in range(n + 1):
    roads.append([])
for i in range(m):
    a, b = (map(int, stdin.readline().split()))
    roads[a].append([a, b])
# print(roads)

goal = [int(1e9)] * (n + 1)
goal[x] = 0

q = deque()
count = 1
for item in roads[x]:
    q.append(item)
flag = True
result = []
while q:
    road = q.popleft()

    if goal[road[1]] == int(1e9):
        goal[road[1]] = goal[road[0]] + 1
        for item in roads[road[1]]:
            q.append(item)

for i in range(1, n + 1):
    if goal[i] == k:
        print(i)
        flag = False

if flag:
    print(-1)
