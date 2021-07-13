# 5
# 14
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 3 5 10
# 3 1 8
# 1 4 2
# 5 1 7
# 3 4 2
# 5 2 4

# https://www.acmicpc.net/problem/11404

from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())
matrix = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    if matrix[a][b] > c:
        matrix[a][b] = c

for i in range(1, n + 1):
    matrix[i][i] = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if j == k:
                continue
            matrix[j][k] = min(matrix[j][k], matrix[j][i] + matrix[i][k])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if matrix[i][j] == int(1e9):
            print(0, end=' ')
        else:
            print(matrix[i][j], end=' ')
    print()