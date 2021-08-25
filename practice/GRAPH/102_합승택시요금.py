# https://programmers.co.kr/learn/courses/30/lessons/72413

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF

    dp = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][i] = 0

    for fare in fares:
        c,d,f = fare
        dp[c][d] = f
        dp[d][c] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j: continue
                dp[i][j] = min(dp[i][k] + dp[k][j], dp[i][j])

    for k in range(1, n + 1):
        answer = min(dp[s][k] + dp[k][a] + dp[k][b], answer)

    return answer

n = 7
s = 3
a = 4
b = 1
fares = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
print(solution(n, s, a, b, fares))