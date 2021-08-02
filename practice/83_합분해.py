# 20 2

# https://www.acmicpc.net/problem/2225

n, k = map(int, input().split())
dp = [[1] * (n*k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(i, i + k - 1):
        if i == j:
            dp[i][j] = i + 1
            continue
        #print(i, j)
        dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

# for i in range(2 * k + 1):
#     for j in range(2 * n + 1):
#         print(dp[i][j], end=' ')
#     print()
# print()

print(dp[n][n + k - 2] % 1000000000)