# https://www.acmicpc.net/problem/5569
# https://huiung.tistory.com/136

MOD = 100000

w, h = map(int, input().split())

dp = [[[[0] * 2 for _ in range(2)] for _ in range(w + 1)] for _ in range(h + 1)]

for i in range(2, h + 1):
    dp[i][1][0][0] = 1

for j in range(2, w + 1):
    dp[1][j][0][1] = 1

# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         print(dp[i][j][0][0], dp[i][j][0][1], end='  ')
#     print()
#     for j in range(1, w + 1):
#         print(dp[i][j][1][0], dp[i][j][1][1], end='  ')
#     print()
#     print()

for i in range(2, h + 1):
    for j in range(2, w + 1):
        dp[i][j][0][0] = (dp[i-1][j][0][0] + dp[i-1][j][1][0]) % MOD
        dp[i][j][0][1] = (dp[i][j-1][0][1] + dp[i][j-1][1][1]) % MOD
        dp[i][j][1][0] = (dp[i-1][j][0][1]) % MOD
        dp[i][j][1][1] = dp[i][j-1][0][0] % MOD

# for i in range(1, h + 1):
#     for j in range(1, w + 1):
#         print(dp[i][j][0][0], dp[i][j][0][1], end='  ')
#     print()
#     for j in range(1, w + 1):
#         print(dp[i][j][1][0], dp[i][j][1][1], end='  ')
#     print()
#     print()

ans = 0
for i in range(2):
    for j in range(2):
        ans += dp[h][w][i][j]

print(ans % MOD)