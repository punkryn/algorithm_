# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5

# https://www.acmicpc.net/problem/1932

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

result = [[0] * i for i in range(1, n + 1)]

result[0][0] = tri[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            result[i][j] = tri[i][j] + result[i - 1][j]
        elif j == i:
            result[i][j] = tri[i][j] + result[i - 1][j - 1]
        else:
            result[i][j] = tri[i][j] + max(result[i - 1][j - 1], result[i - 1][j])


print(max(result[-1]))