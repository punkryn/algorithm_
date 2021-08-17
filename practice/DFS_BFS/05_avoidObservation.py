# 5
# X S X X T
# T X S X X
# X X X X X
# X T X X X
# X X T X X

# https://www.acmicpc.net/problem/18428

import copy
from itertools import combinations

def dfs(hall, start, d):
    x, y = start
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < n and 0 <= ny < n:
        if hall[nx][ny] == 'X' or hall[nx][ny] == 'S' or hall[nx][ny] == 'T':
            hall[nx][ny] = 'T'
            dfs(hall, [nx, ny], d)


def check(blank, hall, teacher, student):
    _hall = copy.deepcopy(hall)
    for x, y in blank:
        _hall[x][y] = 'O'

    for x, y in teacher:
        for i in range(4):
            dfs(_hall, [x, y], i)

    answer = True
    for x, y in student:
        if _hall[x][y] == 'T':
            answer = False
            return answer

    return answer

def show(hall):
    for i in range(len(hall)):
        for j in range(len(hall)):
            print(hall[i][j], end=' ')
        print()
    print()

n = int(input())
hall = [list(input().split()) for _ in range(n)]

blanks = [[x, y] for x in range(n) for y in range(n) if hall[x][y] == 'X']
student = [[x, y] for x in range(n) for y in range(n) if hall[x][y] == 'S']
teacher = [[x, y] for x in range(n) for y in range(n) if hall[x][y] == 'T']

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

flag = True
for blank in combinations(blanks, 3):
    if check(blank, hall, teacher, student):
        print('YES')
        flag = False
        break

if flag:
    print('NO')