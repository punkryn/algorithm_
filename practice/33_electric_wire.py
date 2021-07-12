# 8
# 1 8
# 3 9
# 2 2
# 4 1
# 6 4
# 10 10
# 9 7
# 7 6

# https://www.acmicpc.net/problem/2565

n = int(input())

pole = [list(map(int, input().split())) for _ in range(n)]

pole.sort()
#print(pole)
# dp = [1] * n
# # dp[0] = 1
# for i in range(1, n):
#     for j in range(i):
#         if pole[i][1] > pole[j][1]:
#             dp[i] = max(dp[i], dp[j] + 1)
#
# print(n - max(dp))
#

from bisect import bisect
dp = [pole[0][1]]

for i in range(1, n):
    if dp[-1] < pole[i][1]:
        dp.append(pole[i][1])
    else:
        dp[bisect(dp, pole[i][1])] = pole[i][1]

print(n - len(dp))