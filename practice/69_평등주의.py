# 2
# 5 5
# 4 2 3 7 6
# 5 4
# 4 2 3 7 8

import copy
import sys
sys.stdin = open("./input\\peace.txt", "r")

def check(p):
    tmp = k
    A_ = copy.deepcopy(A)
    for i in range(1, n):
        gap = abs(A_[i] - A_[i+1])
        if gap > p:
            if A_[i] > A_[i+1]:
                #a - b - x = p
                #a - b - p = x
                tmp -= (A_[i] - A_[i+1] - p)
                A_[i] = A_[i+1] + p
                if A[i] < 1:
                    break
            else:
                tmp -= (A_[i + 1] - A_[i] - p)
                A_[i+1] = A_[i] + p
                if A_[i+1] < 1:
                    break
        if tmp < 0:
            return False

    for i in range(n, 1, -1):
        gap = abs(A_[i-1] - A_[i])
        if gap > p:
            if A_[i] > A_[i - 1]:
                tmp -= (A_[i] - A_[i - 1] - p)
                A_[i] = A_[i - 1] + p
                if A[i] < 1:
                    break
            else:
                tmp -= (A_[i - 1] - A_[i] - p)
                A_[i - 1] = A_[i] + p
                if A_[i - 1] < 1:
                    break
        if tmp < 0:
            return False

    return tmp >= 0

MAX = int(1e10)

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    A = [0] * (n + 1)

    for i, a in enumerate(map(int, input().split()), start=1):
        A[i] = a
    #print(A)

    s = 0
    e = MAX

    while s < e:
        mid = (s + e) // 2
        #print(s, e, mid)

        if check(mid):
            #print(True)
            e = mid
        else:
            s = mid + 1

    # if check(e):
    #     s = e

    print("#" + str(test_case), s)