# 7 1 2 3 4 5 6 7
# 8 1 2 3 5 8 13 21 34
# 0

# https://www.acmicpc.net/problem/6603

import copy

def bt(depth, arr, s):
    if depth == 6:
        for i in arr:
            print(i, end=' ')
        print()
        return

    tmp = copy.deepcopy(s)
    while tmp:
        i = tmp.pop(0)
        arr.append(i)
        bt(depth + 1, arr, tmp)
        arr.pop()

while True:
    case = list(map(int, input().split()))
    if case[0] == 0:
        break

    k = case[0]
    s = case[1:]

    bt(0, [], s)
    print()