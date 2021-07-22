# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

# https://www.acmicpc.net/problem/2206

from sys import stdin
from collections import deque

n, m = map(int, input().split())
# _map = [[] for _ in range(n)]
# for i in range(n):
#     for w in stdin.readline().strip():
#         _map[i].append(w)

_map = []
for i in range(n):
    _map.append(list(map(int, list(stdin.readline().strip()))))

#print(_map)

answer = -1

visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

q = deque()
q.append([0, 0, 1])
visited[0][0][1] = 1

while q:
    x, y, dist = q.popleft()

    # for a in range(n):
    #     for b in range(m):
    #         print(visited[a][b], end=' ')
    #     print()
    # print()

    if x == n - 1 and y == m - 1:
        answer = visited[x][y][dist]
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if _map[nx][ny] == 1 and dist == 1:
                visited[nx][ny][0] = visited[x][y][1] + 1
                q.append([nx, ny, 0])
            elif _map[nx][ny] == 0 and visited[nx][ny][dist] == 0:
                visited[nx][ny][dist] = visited[x][y][dist] + 1
                q.append([nx, ny, dist])

print(answer)