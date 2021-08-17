# https://www.acmicpc.net/problem/17142

from sys import stdin
from itertools import combinations
from collections import deque
input = stdin.readline

def bfs(virus):
    count = 0
    lab_ = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if lab[i][j] == 0:
                continue
            elif lab[i][j] == 1:
                lab_[i][j] = '-'
                count += 1
            elif lab[i][j] == 2:
                lab_[i][j] = '*'
                count += 1

    q = deque()
    for v in virus:
        x, y = v
        lab_[x][y] = 0
        q.append((x, y, 0))

    ans = 0
    flag = False
    # print(count)

    if count == n * n:
        return 0

    while q:
        x, y, t = q.popleft()
        ans = max(ans, t)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if lab_[nx][ny] != '-' and (lab_[nx][ny] == -1 or lab_[nx][ny] == '*'):
                    if lab_[nx][ny] != '*':
                        count += 1
                    lab_[nx][ny] = t + 1

                    if count == n * n:
                        ans = max(ans, t + 1)
                        flag = True
                        break

                    q.append((nx, ny, t + 1))

        if flag:
            break
    # print(ans, count)
    # for i in range(len(lab_)):
    #     print(lab_[i])
    # print()

    if count != n * n:
        ans = -1

    return ans

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
virus_pos = []
for i in range(n):
    for j in range(n):
        if lab[i][j] == 2:
            virus_pos.append((i, j))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = int(1e9)
result = []
for comb in combinations(virus_pos, m):
    tmp = bfs(list(comb))
    if tmp == -1:
        ans = -1
    else:
        result.append(tmp)

if result:
    ans = min(result)

print(ans)