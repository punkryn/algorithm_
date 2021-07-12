# 6
# 4 2 6 3 1 5

# https://www.acmicpc.net/problem/2352

from bisect import bisect

n = int(input())
line = list(map(int, input().split()))

dp = [line[0]]
for i in range(1, n):
    if dp[-1] < line[i]:
        dp.append(line[i])
    else:
        dp[bisect(dp, line[i])] = line[i]
    # print(dp)

print(len(dp))