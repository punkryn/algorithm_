def editDistance(S, T):
    m = len(S)
    n = len(T)

    E = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        E[i][0] = i

    for j in range(n + 1):
        E[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            E[i][j] = min(E[i][j - 1] + 1, E[i - 1][j] + 1, E[i - 1][j - 1] + (0 if S[i - 1] == T[j - 1] else 1))

    for i in range(m + 1):
        for j in range(n + 1):
            print(E[i][j], end=' ')
        print()
    print()
    return E[m][n]

S = 'daphnia'
T = 'adelphia'
print(editDistance(S, T))