# 5 5
# 1 2 3 4 5
# 5 4 3 2 1
# 2 3 4 5 6
# 6 5 4 3 2
# 1 2 1 2 1

# https://www.acmicpc.net/problem/14500

from sys import stdin

def dfs(depth, x, y):
    if depth == 4:
        return paper[x][y]

    total = 0

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            total = max(total, paper[x][y] + dfs(depth + 1, nx, ny))
            visited[nx][ny] = 0

    return total

def middle(x, y):
    result = 0
    if x >= 1 and y >= 1 and y < m - 1:
        result = max(result, paper[x][y-1] + paper[x][y] + paper[x-1][y] + paper[x][y+1])

    if x >= 1 and x < n - 1 and y < m - 1:
        #print(x, y)
        result = max(result, paper[x-1][y] + paper[x][y] + paper[x + 1][y] + paper[x][y + 1])

    if x >= 0 and x < n - 1 and y < m - 1:
        result = max(result, paper[x][y - 1] + paper[x][y] + paper[x][y + 1] + paper[x + 1][y])

    if x >= 1 and x < n - 1 and y >= 1:
        result = max(result, paper[x - 1][y] + paper[x][y] + paper[x + 1][y] + paper[x][y - 1])

    return result


n, m = map(int, input().split())

paper = []
for _ in range(n):
    row = list(map(int, stdin.readline().split()))
    paper.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0] * m for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        result = max(result, dfs(1, i, j))
        result = max(result, middle(i, j))
        visited[i][j] = 0

print(result)