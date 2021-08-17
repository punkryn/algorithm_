# 5 4
# 0 0 1 0 2
# 2 3 2 1 0
# 4 3 2 9 0
# 1 0 2 9 0
# 8 8 2 1 0
# 1 3
# 3 4
# 8 1
# 4 8

# https://www.acmicpc.net/problem/21610

def move_cloud(d, s):
    tmp = []
    for cloud in clouds:
        r, c = cloud
        nr = r + (dx[d] * s)
        nc = c + (dy[d] * s)

        if 0 <= nr < n and 0 <= nc < n:
            tmp.append([nr, nc])
        else:
            #print(r, c, nr, nc)
            if -n > nr:
                nr %= -n

            if -n > nc:
                nc %= -n

            if nr - n >= n:
                nr %= n
                nr += n

            if nc - n >= n:
                nc %= n
                nc += n

            if nr < 0 and 0 <= nc < n:
                tmp.append([n + nr, nc])
            elif nr >= n and 0 <= nc < n:
                tmp.append([nr - n, nc])
            elif 0 <= nr < n and nc < 0:
                tmp.append([nr, n + nc])
            elif 0 <= nr < n and nc >= n:
                tmp.append([nr, nc - n])
            elif nr < 0 and nc < 0:
                tmp.append([n + nr, n + nc])
            elif nr >= n and nc >= n:
                tmp.append([nr - n, nc - n])
            elif nr < 0 and nc >= n:
                tmp.append([n + nr, nc - n])
            elif nr >= n and nc < 0:
                tmp.append([nr - n, n + nc])
    return tmp

def rain():
    for cloud in clouds:
        r, c = cloud
        A[r][c] += 1

def water_copy_bug():
    for cloud in prev:
        r, c = cloud

        count = 0
        for i in [1, 3, 5, 7]:
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < n and 0 <= nc < n:
                if A[nr][nc] > 0:
                    count += 1

        A[r][c] += count

def make_cloud():
    for i in range(n):
        for j in range(n):
            if A[i][j] >= 2 and [i, j] not in prev:
                clouds.append([i, j])
                A[i][j] -= 2

from sys import stdin
import copy

n, m = map(int, input().split())

A = [list(map(int, stdin.readline().split())) for _ in range(n)]
info = [list(map(int, stdin.readline().split())) for _ in range(m)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

for inf in info:
    d, s = inf

    clouds = move_cloud(d - 1, s)
    print(clouds)
    rain()

    prev = copy.deepcopy(clouds)
    clouds = []

    water_copy_bug()
    make_cloud()
    print('1', clouds)

total = 0
for i in range(n):
    for j in range(n):
        total += A[i][j]
print(total)