def knapsack(n, C):
    ln = len(n)
    K = [[0] * (C + 1) for _ in range(ln + 1)]

    for i in range(1, ln + 1):
        for w in range(1, C + 1):
            if n[i - 1][0] > w:
                K[i][w] = K[i - 1][w]
            else:
                K[i][w] = max(K[i - 1][w], K[i - 1][w - n[i - 1][0]] + n[i - 1][1])

    for i in range(ln + 1):
        for j in range(C + 1):
            print(K[i][j], end=' ')
        print()
    print()

    return K[ln][C]

n = [[5, 10], [4, 40], [6, 30], [3, 50]]
C = 10
print(knapsack(n, C))