# 3 1

# https://www.acmicpc.net/problem/15649

import copy

n, m = map(int, input().split())

def per(n, cur, m, arr, depth):
    if depth == m:
        for num in arr:
            print(num, end=' ')
        print()
        return
    else:
        tmp = copy.deepcopy(cur)
        for j in range(n):
            if tmp[j] == 0:
                continue
            tmp[j] = 0
            arr.append(j + 1)

            per(n, tmp, m, arr, depth + 1)

            arr.pop()
            tmp[j] = j + 1

cur = [i for i in range(1, n + 1)]
per(n, cur, m, [], 0)