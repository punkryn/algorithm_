# https://www.acmicpc.net/problem/14501

n = int(input())
serve = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(1, i + 1):
        if serve[j-1][0] + j - 1 == i:
            dp[i] = max(max(dp[:j]) + serve[j-1][1], dp[i])
        # print(i, dp)

print(max(dp))