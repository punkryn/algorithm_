# 3 3
# 1 1 0
# 1 1 1
# 1 0 1
# 1 1 1

# https://www.acmicpc.net/problem/14503

n, m = map(int, input().split())

r, c, d = map(int, input().split())

room = [list(map(int, input().split())) for _ in range(n)]

# 북 동 남 서
# 0 1 2 3

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = []
answer = 1
q.append([r, c, d, 0, answer])

while q:
    row, col, di, count, ans = q.pop(0)
    room[row][col] = 2

    nd = (di - 1) % 4
    nx = row + dx[nd]
    ny = col + dy[nd]

    # for kk in range(n):
    #     for ll in range(m):
    #         print(room[kk][ll], end=' ')
    #     print()
    # print()

    if count == 4:
        nd = (di + 2) % 4
        nx = row + dx[nd]
        ny = col + dy[nd]

        if room[nx][ny] != 1:
            q.append([nx, ny, di, 0, ans])
            continue
        elif room[nx][ny] == 1:
            answer = ans
            break

    if room[nx][ny] == 0:
        q.append([nx, ny, nd, 0, ans + 1])
    elif room[nx][ny] != 0:
        q.append([row, col, nd, count + 1, ans])

print(answer)