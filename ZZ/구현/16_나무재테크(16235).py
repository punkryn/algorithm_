# 1 1 1
# 1
# 1 1 1

# https://www.acmicpc.net/problem/16235

from collections import deque
from sys import stdin

def spring():
    global count

    for i in range(n):
        for j in range(n):
            length = len(grounds[i][j])
            for k in range(length):
                age = grounds[i][j][k]
                if age <= yang[i][j]:
                    yang[i][j] -= age
                    grounds[i][j][k] += 1
                else:
                    for _ in range(k, length):
                        yang[i][j] += grounds[i][j].pop() // 2
                        count -= 1
                    break

def autumn():
    global count
    for i in range(n):
        for j in range(n):
            if grounds[i][j]:
                for age in (grounds[i][j]):
                    if age % 5 == 0:
                        for l in range(8):
                            nx = i + dx[l]
                            ny = j + dy[l]
                            if 0 <= nx < n and 0 <= ny < n:
                                grounds[nx][ny].appendleft(1)
                                count += 1

            yang[i][j] += A[i][j]


n, m, k = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for _ in range(n)]
# trees = [list(map(int, stdin.readline().split())) for _ in range(m)]

yang = [[5] * (n + 1) for _ in range(n + 1)]

grounds = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    grounds[x-1][y-1].append(z)

dx = [-1, 1, 0, 0, -1, 1, 1, -1]
dy = [0, 0, -1, 1, 1, 1, -1, -1]

count = m
for _ in range(k):
    spring()
    autumn()

print(count)