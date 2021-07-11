# def solution(n):
#     answer = 0
#
#     dp = [0] * (n // 4 + 1 if n % 4 != 0 else n // 4)
#
#     start = n % 4 if n % 4 != 0 else 4
#     dp[0] = start
#     for i in range(1, len(dp)):
#         start += 4
#         dp[i] = dp[i - 1] * (start)
#
#     print(dp)
#     answer = dp[-1]
#     return answer
#
# # 4 8 12 16 20
# # 1 5 9 13 17 21
# n = 20
# print(solution(n))

# https://www.acmicpc.net/problem/10872

# n = int(input())
#
# dp = [1] * (n + 1)
#
# for i in range(2, n + 1):
#     dp[i] = dp[i-1] * i
#
#
# print(dp[-1])

n = int(input())

start = 1
for i in range(2, n + 1):
    start *= i
print(start)