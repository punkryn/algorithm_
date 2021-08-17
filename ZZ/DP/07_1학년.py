# 11
# 8 3 2 4 8 7 2 4 0 8 8

# https://www.acmicpc.net/problem/5557

n = int(input())
formula = list(map(int, input().split()))

dp = [[0] * 21 for _ in range(n + 1)]

dp[0][formula[0]] = 1

for i in range(1, n):
    for j in range(21):
        if dp[i-1][j] != 0:
            sum_ = j + formula[i]
            if sum_ <= 20:
                dp[i][sum_] += dp[i-1][j]

            sub_ = j - formula[i]
            if sub_ >= 0:
                dp[i][sub_] += dp[i-1][j]

# for i in range(n):
#     for j in range(21):
#         print(dp[i][j], end=' ')
#     print()
# print()
print(dp[n-2][formula[n-1]])