# 7
# 3 10
# 5 20
# 1 10
# 1 20
# 2 15
# 4 40
# 2 200

# https://www.acmicpc.net/problem/14501

n = int(input())
schedule = [list(map(int, input().split())) for _ in range(n)]

dp = [0] * (n + 5)

for i in range(n):
    result = max(dp[:i]) if i > 0 else 0
    while True:
        result += schedule[i][1]
        i += schedule[i][0]
        dp[i - 1] = max(dp[i - 1], result)

        if i >= n:
            break
print(max(dp[:n]))