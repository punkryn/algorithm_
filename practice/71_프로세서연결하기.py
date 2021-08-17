# 1
# 7
# 0 0 1 0 0 0 0
# 0 0 1 0 0 0 0
# 0 0 0 0 0 1 0
# 0 0 0 0 0 0 0
# 1 1 0 1 0 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 0 0

#import sys
#sys.stdin = open("input.txt", "r")

def dfs(depth, total, count):
    global ans
    global ans2
    global maxcount
    #print(depth, total, count)
    if count + len(cells) - depth < maxcount:
        return

    if depth == len(cells):
        if count == len(cells):
            ans = min(ans, total)
        ans2 = min(ans, total)
        maxcount = max(maxcount, count)
        return

    #show()

    x, y = cells[depth]

    if x == 0 or y == 0 or x == n - 1 or y == n - 1:
        dfs(depth + 1, total, count + 1)
        return

    for i in range(4):
        init()
        #print(x, y, i)
        connect(x, y, i)
        #print(flag)
        if not flag:
            dfs(depth + 1, total + length, count + 1)
            disconnect(x, y, i)
        else:
            matrix[x][y] = 1
            dfs(depth + 1, total, count)

def connect(x, y, i):
    global flag
    global length
    nx = x + dx[i]
    ny = y + dy[i]

    if not (0 <= nx < n and 0 <= ny < n):
        return

    if matrix[nx][ny] == 0:
        matrix[nx][ny] = 2
        length += 1
        connect(nx, ny, i)
    else:
        flag = True
        length = 0

    if flag:
        matrix[x][y] = 0

def disconnect(x, y, i):
    nx = x + dx[i]
    ny = y + dy[i]

    while (0 <= nx < n and 0 <= ny < n):
        matrix[nx][ny] = 0
        nx += dx[i]
        ny += dy[i]

def init():
    global flag
    global length
    flag = False
    length = 0

T = int(input())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
MAX = int(1e10)

for test_case in range(1, T + 1):
    flag = False
    flag2 = False
    length = 0
    maxcount = 0
    ans = MAX
    ans2 = MAX

    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    cells = [[i, j] for i in range(n) for j in range(n) if matrix[i][j] == 1]
    #visited = [[0] * n for _ in range(n)]
    dfs(0, 0, 0)

    if ans < MAX:
        answer = ans
    else:
        answer = ans2

    print("#" + str(test_case), answer)