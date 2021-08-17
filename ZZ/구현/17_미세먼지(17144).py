# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0

# https://www.acmicpc.net/problem/17144

import copy

def spread():
    tmp = [[0] * c for _ in range(r)]
    tmp[purifier[0]][0] = -1
    tmp[purifier[1]][0] = -1

    for i in range(r):
        for j in range(c):
            count = 0
            if A[i][j] > 0:
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]

                    if 0 <= nx < r and 0 <= ny < c and A[nx][ny] != -1:
                        count += 1
                        tmp[nx][ny] += A[i][j] // 5

                tmp[i][j] += (A[i][j] - A[i][j] // 5 * count)
    return tmp

def purify():
    tmp = copy.deepcopy(A)
    col = 1
    row = purifier[0]
    tmp[row][col] = 0

    for i in range(4):
        while 0 <= row + dx[i] < r and 0 <= col + dy[i] < c:
            if A[row + dx[i]][col + dy[i]] == -1:
                break

            tmp[row + dx[i]][col + dy[i]] = A[row][col]
            row += dx[i]
            col += dy[i]

    col = 1
    row = purifier[1]
    tmp[row][col] = 0
    for i in [0, 3, 2, 1]:
        while 0 <= row + dx[i] < r and 0 <= col + dy[i] < c:
            if A[row + dx[i]][col + dy[i]] == -1:
                break

            tmp[row + dx[i]][col + dy[i]] = A[row][col]
            row += dx[i]
            col += dy[i]
    return tmp


r, c, t = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(r)]

purifier = []
for i in range(2, r - 2):
    if A[i][0] == -1:
        purifier.append(i)

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for _ in range(t):
    A = spread()
    A = purify()

total = 0
for i in range(r):
    for j in range(c):
        if A[i][j] == -1:
            continue
        total += A[i][j]
#         print(A[i][j], end=' ')
#     print()
# print()
print(total)