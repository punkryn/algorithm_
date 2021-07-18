# https://www.acmicpc.net/contest/problem/658/6

d, m = map(int, input().split())

dp = [[0] * (d // 2 + 1) for _ in range(d // 2 + 1)]

for i in range(d // 2 + 1):
    dp[0][i] = 1

for i in range(1, d // 2 + 1):
    for j in range(i + 1, d // 2 + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[-2][-1])