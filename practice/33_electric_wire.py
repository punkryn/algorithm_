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
dp = [1] * n
# dp[0] = 1
for i in range(1, n):
    for j in range(i):
        if pole[i][1] > pole[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))

# from bisect import bisect
#
# arr = [2, 1, 3, 5, 4]
# lis = []
# lis.append(arr[0])
# print(lis)
#
# for n in range(1, len(arr)):
#     if lis[-1] < arr[n]:
#         lis.append(arr[n])
#     else:
#         lis[bisect(lis, arr[n])] = arr[n]
#     print(lis)