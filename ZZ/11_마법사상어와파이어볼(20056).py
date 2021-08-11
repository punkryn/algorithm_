# 4 2 1
# 1 1 5 2 2
# 1 4 7 1 6

# https://www.acmicpc.net/problem/20056

from collections import deque

def move():
    tmp = set()
    for fireball in fireballs:
        r, c, m, s, d = fireball
        nr = r + (dx[d] * s)
        nc = c + (dy[d] * s)

        if 1 <= nr <= n and 1 <= nc <= n:
            grid[nr][nc].append((nr, nc, m, s, d))
            tmp.add(str(nr) + ' ' + str(nc))
        else:
            while nr <= -n:
                nr = (nr + n)

            while nc <= -n:
                nc = nc + n

            while nc - n > n:
                nc = nc - n

            while nr - n > n:
                nr = nr - n

            if nr <= 0 and 1 <= nc <= n:
                grid[n + nr][nc].append((n + nr, nc, m, s, d))
                tmp.add(str(n + nr) + ' ' + str(nc))
            elif nr > n and 1 <= nc <= n:
                grid[nr - n][nc].append((nr - n, nc, m, s, d))
                tmp.add(str(nr - n) + ' ' + str(nc))
            elif nc <= 0 and 1 <= nr <= n:
                grid[nr][n + nc].append((nr, n + nc, m, s, d))
                tmp.add(str(nr) + ' ' + str(n + nc))
            elif nc > n and 1 <= nr <= n:
                grid[nr][nc - n].append((nr, nc - n, m, s, d))
                tmp.add(str(nr) + ' ' + str(nc - n))
            elif nr <= 0 and nc <= 0:
                grid[n + nr][n + nc].append((n + nr, n + nc, m, s, d))
                tmp.add(str(n + nr) + ' ' + str(n + nc))
            elif nr > n and nc > n:
                grid[nr - n][nc - n].append((nr - n, nc - n, m, s, d))
                tmp.add(str(nr - n) + ' ' + str(nc - n))
            elif nr <= 0 and nc > n:
                grid[n + nr][nc - n].append((n + nr, nc - n, m, s, d))
                tmp.add(str(n + nr) + ' ' + str(nc - n))
            elif nr > n and nc <= 0:
                grid[nr - n][n + nc].append((nr - n, n + nc, m, s, d))
                tmp.add(str(nr - n) + ' ' + str(n+nc))

    return tmp

def process(nextSet):
    nextSet = list(nextSet)

    for nxt in nextSet:
        global total
        r, c = map(int, nxt.split())

        if len(grid[r][c]) >= 2:
            totalM = 0
            totalS = 0
            j = h = 0
            length = len(grid[r][c])

            for g in grid[r][c]:
                _, _, m, s, d = g
                totalM += m
                totalS += s
                if d % 2 == 0:
                    j += 1
                else:
                    h += 1

            grid[r][c] = []

            newM = totalM // 5
            newS = totalS // length
            if j == length or h == length:
                newD = [0, 2, 4, 6]
            else:
                newD = [1, 3, 5, 7]

            if newM == 0:
                total -= totalM
                continue
            else:
                total -= (totalM)
                total += newM * 4
                for direction in newD:
                    fireballs.append([r, c, newM, newS, direction])
        else:
            fireballs.append(grid[r][c][0])
            grid[r][c] = []

from sys import stdin

n, m, k = map(int, input().split())

fireballs = [list(map(int, stdin.readline().split())) for _ in range(m)]

grid = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

total = 0
for fireball in fireballs:
    _, _, m, _, _ = fireball
    total += m

for _ in range(k):
    # for i in range(1, n + 1):
    #     for j in range(1, n + 1):
    #         print(grid[i][j], end=' ')
    #     print()
    # print()
    nextSet = move()
    fireballs = []
    #print(nextSet)
    process(nextSet)
    # print(fireballs)

print(total)