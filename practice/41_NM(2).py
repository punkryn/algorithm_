# 3 1

# https://www.acmicpc.net/problem/15650

import copy

n, m = map(int, input().split())

def comb(depth, ans, arr):
    if depth == m:
        for i in ans:
            print(i, end=' ')
        print()
        return

    tmp = copy.deepcopy(arr)
    while tmp:
        i = tmp.pop(0)
        ans.append(i)
        comb(depth + 1, ans, tmp)
        ans.pop()


arr = [i for i in range(1, n + 1)]
comb(0, [], arr)