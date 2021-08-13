# 2 0 3

# https://www.acmicpc.net/problem/15684

def go(x, depth, lim):
    global flag
    if flag:
        return

    if depth == lim:
        possible = True
        for i in range(1, n + 1):
            col = i
            for j in range(1, h + 1):
                if ladder[j][col]:
                    col += 1
                elif ladder[j][col-1]:
                    col -= 1

            if i != col:
                possible = False
                break

        if possible:
            flag = True
        return

    for i in range(x, h + 1):
        for j in range(1, n + 1):
            if ladder[i][j-1] == 0 and ladder[i][j] == 0 and ladder[i][j+1] == 0:
                ladder[i][j] = 1
                go(i, depth + 1, lim)
                ladder[i][j] = 0


n, m, h = map(int, input().split())

rows = [list(map(int, input().split())) for _ in range(m)]

ladder = [[0] * (n + 2) for _ in range(h + 2)]
visited = [[0] * (n + 2) for _ in range(h + 2)]

for i, row in enumerate(rows, start=1):
    a, b = row
    ladder[a][b] = i

flag = False
ans = 10

for i in range(3+1):
    # print(i)
    go(1, 0, i)
    if flag:
        ans = i
        print(ans)
        break

if ans == 10:
    print(-1)
