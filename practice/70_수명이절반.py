def check(mid):
    now = 1
    cnt = 0
    for i in range(1, n + 1):
        #print(i, now, cnt, S[now])
        if W[i] <= mid:
            cnt += 1
        else:
            cnt = 0

        if cnt == S[now]:
            cnt = 0

            now += 1
            if now > k:
                break

    #print(now, k)
    return now > k

import sys

sys.stdin = open("input\\lifetime.txt", "r")

T = int(input())
MAX = 200001

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    W = [0] * MAX
    for i, w in enumerate(map(int, input().split()), start=1):
        W[i] = w

    S = [0] * MAX
    for i, s in enumerate(map(int, input().split()), start=1):
        S[i] = s


    left = 1
    right = MAX
    while left < right:
        mid = (left + right) // 2

        if check(mid):
            right = mid
        else:
            left = mid + 1

    print("#" + str(test_case), left)