# https://www.acmicpc.net/problem/17143

from sys import stdin
from collections import deque



def shark_move():
    tmp2 = [[deque() for _ in range(c+1)] for _ in range(r+1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if grid[i][j]:
                shark = grid[i][j].popleft()
                #print(shark, r, c)
                s, d, z = shark
                if d == 1:
                    if s > (i - 1):
                        tmp = (s - i + 1) % (r * 2 - 2)
                        if tmp <= (r * 2 - 2) // 2 and tmp != 0:
                            tmp2[1 + tmp][j].append([s, d + 1, z])
                        else:
                            if tmp == 0:
                                tmp2[tmp + 1][j].append([s, d, z])
                            else:
                                tmp2[2 * r - tmp - 1][j].append([s, d, z])
                    else:
                        tmp2[i-s][j].append([s, d, z])
                elif d == 3:
                    #print(i, j, s, d, z)
                    if s > (c - j):
                        tmp = (s - c + j) % (c * 2 - 2)
                        if tmp <= (c * 2 - 2) // 2 and tmp != 0:
                            tmp2[i][c - tmp].append([s, d + 1, z])
                        else:
                            if tmp == 0:
                                tmp2[i][c].append([s, d, z])
                            else:
                                tmp2[i][tmp-(c * 2 - 2)//2 + 1].append([s, d, z])
                    else:
                        tmp2[i][j+s].append([s, d, z])
                elif d == 2:
                    print(123)
                    if s > (r - i):
                        tmp = (s - r + i) % (r * 2 - 2)
                        if tmp <= (r * 2 - 2) // 2 and tmp != 0:
                            tmp2[r - tmp +1][j].append([s, d - 1, z])
                        else:
                            if tmp == 0:
                                tmp2[r][j].append([s, d, z])
                            else:
                                if r == i:
                                    tmp2[tmp - (r * 2 - 2)//2 + 1][j].append([s, d, z])
                                else:
                                    tmp2[tmp-(r * 2 - 2)//2-1][j].append([s, d, z])
                    else:
                        tmp2[i+s][j].append([s, d, z])
                elif d == 4:
                    if s > (j - 1):
                        tmp = (s - j + 1) % (c * 2 - 2)
                        if tmp <= (c * 2 - 2) // 2 and tmp != 0:
                            tmp2[i][tmp + 1].append([s, d - 1, z])
                        else:
                            if tmp == 0:
                                tmp2[i][tmp + 1].append([s, d, z])
                            else:
                                tmp2[i][2 * c - tmp - 1].append([s, d, z])
                    else:
                        tmp2[i][j - s].append([s, d, z])
    return tmp2

def eat():
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if len(grid[i][j]) >= 2:
                maxvalue = max(grid[i][j], key=lambda x: x[2])
                # print('max', maxvalue)
                grid[i][j] = deque([maxvalue])


input = stdin.readline

r, c, m = map(int, input().split())
grid = [[deque() for _ in range(c + 1)] for _ in range(r + 1)]
sharks = deque()
for _ in range(m):
    r_, c_, s_, d_, z_ = map(int, input().split())
    grid[r_][c_].append([s_, d_, z_])
    sharks.append([r_, c_, s_, d_, z_])

dx = [10, -1, 1, 0, 0]
dy = [10, 0, 0, -1, 1]

# print(len(grid), len(grid[0]))

count = 0
if m > 0:
    for i in range(1, c + 1):
        for j in range(1, r + 1):

            if len(grid[j][i]) > 0:
                s_, d_, z_ = grid[j][i].popleft()
                # print(s_, d_, z_, i, j)
                count += z_
                break

        grid = shark_move()
        eat()

        for x in range(1, r + 1):
            for y in range(1, c + 1):
                print(grid[x][y], end=' ')
            print()
        print()

print(count)