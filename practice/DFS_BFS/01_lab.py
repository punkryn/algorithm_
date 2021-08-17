# https://www.acmicpc.net/problem/14502

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

from itertools import combinations
import copy

def dfs(room, virus):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = []
    stack.append(virus)

    while stack:
        xpos, ypos = stack.pop()

        for i in range(4):
            x = xpos + dx[i]
            y = ypos + dy[i]
            if 0 <= x < n and 0 <= y < m:
                if room[x][y] == 0:
                    room[x][y] = 2
                    stack.append([x, y])

def safezone(room):
    count = 0
    for i in range(n):
        for j in range(m):
            if room[i][j] == 0:
                count += 1
    return count

def show(room):
    for i in range(n):
        for j in range(m):
            print(room[i][j], end=' ')
        print()
    print()

n, m = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

blank = [[i, j] for i in range(n) for j in range(m) if room[i][j] == 0]
virus = [[i, j] for i in range(n) for j in range(m) if room[i][j] == 2]

result = 0
for walls in combinations(blank, 3):
    _room = copy.deepcopy(room)
    for wall in walls:
        x, y = wall
        _room[x][y] = 1

    for v in virus:
        dfs(_room, v)
        # show(_room)

    result = max(safezone(_room), result)

print(result)