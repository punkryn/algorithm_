# 3
# 3
# ..*
# ..*
# **.
# 5
# ..*..
# ..*..
# .*..*
# .*...
# .*...
# 7
# .......
# .....**
# *******
# *******
# *******
# *******
# *******

import sys
from collections import deque

sys.stdin = open("./input/pathfinder.txt", "r")

def show():
    for i in range(n):
        for j in range(n):
            print(visited[i][j], end=' ')
        print()
    print()

def bfs(start):
    q = deque()
    q.append(start)
    visited[start[0]][start[1]] = -1

    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] == -1 or table[nx][ny] == '*':
                continue

            if visited[nx][ny] == 0:
                q.append([nx, ny])

            visited[nx][ny] = -1

def countMine():
    for i in range(n):
        for j in range(n):
            if table[i][j] == '.':
                cnt = 0
                for k in range(8):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < n and 0 <= ny < n and table[nx][ny] == '*':
                        cnt += 1

                visited[i][j] = cnt

T = int(input())

dx = [0, 0, 1, -1, -1, 1, 1, -1]
dy = [1, -1, 0, 0, 1, 1, -1, -1]

for test_case in range(1, T + 1):
    n = int(input())
    table = [list(input().strip()) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    #show()

    # for i in range(n):
    #     for j in range(n):
    #         print(table[i][j], end=' ')
    #     print()
    # print()

    count = 0

    countMine()

    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0 and table[i][j] != '*':
                bfs([i, j])
                count += 1

            #show()


    for i in range(n):
        for j in range(n):
            if visited[i][j] > 0 and table[i][j] != '*':
                #print('123')
                count += 1

    #show()

    print("#" + str(test_case), count)