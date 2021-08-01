# 4 7
# 6 13
# 4 8
# 3 6
# 5 12

# https://www.acmicpc.net/problem/12865

n, k = map(int, input().split())
products = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    w, v = products[i - 1]
    for j in range(1, k + 1):
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j - w] + v)

print(dp[-1][-1])