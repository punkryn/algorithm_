# https://www.acmicpc.net/problem/1256

n, m, k = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, m + 1):
    dp[0][i] = 1

for i in range(1, n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]

word = ''
if dp[n][m] < k:
    print(-1)
else:
    A = n
    Z = m
    skip = k-1
    while not (A == 0 and Z == 0):
        if A == 0:
            for i in range(Z):
                word += 'z'
            Z = 0
            continue

        if Z == 0:
            for i in range(A):
                word += 'a'
            A = 0
            continue

        idx = dp[A-1][Z]
        if skip < idx:
            word += 'a'
            A -= 1
        else:
            word += 'z'
            Z -= 1
            skip -= idx

print(word)