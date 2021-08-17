# 5
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR

# https://www.acmicpc.net/problem/10026

from collections import deque

def bfs(i, j, visit, count, flag):
    q = deque()
    q.append((i, j))
    visit[i][j] = count

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visit[nx][ny] == 0:
                    if flag:
                        if grid[x][y] == grid[nx][ny]:
                            visit[nx][ny] = count
                            q.append((nx, ny))
                    else:
                        if (grid[x][y] == 'B' and grid[nx][ny] == 'B') or (grid[x][y] != 'B' and grid[nx][ny] != 'B'):
                            visit[nx][ny] = count
                            q.append((nx, ny))

n = int(input())

grid = [list(input().strip()) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0] * n for _ in range(n)]
visited2 = [[0] * n for _ in range(n)]

count = 0
count2 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            count += 1
            bfs(i, j, visited, count, True)

        if visited2[i][j] == 0:
            count2 += 1
            bfs(i, j, visited2, count2, False)
print(count, count2)