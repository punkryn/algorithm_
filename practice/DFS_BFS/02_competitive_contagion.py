# 3 3
# 1 0 2
# 0 0 0
# 3 0 0
# 2 3 2

# 5 4
# 1 0 0 0 2
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 3 0 0 0 4
# 3 3 3

# https://www.acmicpc.net/problem/18405

from collections import deque
from sys import stdin

n, k = map(int, stdin.readline().split())
tube = [list(map(int, stdin.readline().split())) for _ in range(n)]
s, x, y = map(int, stdin.readline().split())

# virus = [[] for _ in range(k + 1)]
# for a in range(1, k + 1):
#     for x_ in range(n):
#         for y_ in range(n):
#             if tube[x_][y_] == a:
#                 virus[a].append([x_, y_])

q = []
for x_ in range(n):
    for y_ in range(n):
        if tube[x_][y_] != 0:
            q.append([tube[x_][y_], x_, y_, 0])

# q = deque()
# for i in range(1, k + 1):
#     for v in virus[i]:
#         q.append([v, 0])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q.sort()
while q:
    vnum, xpos, ypos, time = q.pop(0)

    if time == s:
        break

    for d in range(4):
        nx = xpos + dx[d]
        ny = ypos + dy[d]
        if 0 <= nx < n and 0 <= ny < n:
            if tube[nx][ny] == 0:
                tube[nx][ny] = vnum
                q.append([vnum, nx, ny, time + 1])

    # for i in range(n):
    #     print(tube[i])
    # print()
print(tube[x-1][y-1])