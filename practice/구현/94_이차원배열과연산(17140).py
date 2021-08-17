# https://www.acmicpc.net/problem/17140

def operR(row, max_len):
    # max_len = len(max(A, key=lambda x: len(x)))

    tmp = [[0] * (max_len * 2) for _ in range(row)]

    maxv = 0
    for i in range(row):
        result = {}
        result2 = []
        # sorted_x = sorted(A[i], key=lambda x: (x.count(), x))
        for j in range(len(A[i])):
            if A[i][j] != 0 and A[i][j] not in result.keys():
                result[A[i][j]] = A[i].count(A[i][j])

        for key in result.keys():
            result2.append((key, result[key]))

        result2.sort(key=lambda x: (x[1], x[0]))

        maxv = max(maxv, len(result2) * 2)
        for k, v in enumerate(result2):
            tmp[i][k * 2] = v[0]
            tmp[i][k * 2 + 1] = v[1]

    # print(tmp)
    return tmp, maxv

def operC(max_row, col):
    tmp = [[0] * (col) for _ in range(max_row * 2)]
    # print(max_row, col)
    maxv = 0
    for i in range(col):
        result = {}
        result2 = []

        for j in range(max_row):
            # print(j, i)
            if A[j][i] != 0 and A[j][i] not in result.keys():
                result[A[j][i]] = 1
            elif A[j][i] != 0 and A[j][i] in result.keys():
                result[A[j][i]] += 1

        for key in result.keys():
            result2.append((key, result[key]))

        result2.sort(key=lambda x: (x[1], x[0]))
        maxv = max(maxv, len(result2) * 2)
        # print(result2)
        for k, v in enumerate(result2):
            tmp[k * 2][i] = v[0]
            tmp[k * 2 + 1][i] = v[1]

    # print(tmp)
    return tmp, maxv


from sys import stdin
input = stdin.readline

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

t = 0
ans = -1
# operR()
# operC(3, 3)
row = 3
col = 3
while t <= 100:
    try:
        if A[r-1][c-1] == k:
            ans = t
            break
    except IndexError:
        pass

    if row >= col:
        A, col_ = operR(row, col)
        col = col_
    else:
        A, row_ = operC(row, col)
        row = row_
    # print(row, col)
    # for _ in range(len(A)):
    #     print(A[_])
    # print()

    t += 1

print(ans)