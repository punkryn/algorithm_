# 3
# 4 5 12
# 2 10 6

# https://www.acmicpc.net/problem/15896

from sys import stdin
input = stdin.readline

INT_MAX = 2147483647
INT_MIN = -2147483647 - 1


def Solve1():
    bitcnt = [0] * 30
    bitsum = [0] * 30

    for i in A:
        for j in range(30):
            base = 1 << j
            if i & base:
                bitcnt[j] += 1

    for i in B:
        for j in range(30):
            base = 1 << j
            if i & base:
                bitsum[j] = (bitsum[j] + bitcnt[j]) % 1999

    ans = 0
    for i in range(30):
        ans += (1 << i) % 1999 * bitsum[i] % 1999
        ans %= 1999

    return ans

def Solve2():
    minA = [[0] * 2 for _ in range(30)]
    minB = [[0] * 2 for _ in range(30)]
    maxA = [[0] * 2 for _ in range(30)]
    maxB = [[0] * 2 for _ in range(30)]

    for i in range(30):
        for j in range(2):
            minA[i][j] = INT_MAX
            maxA[i][j] = INT_MIN
            minB[i][j] = INT_MAX
            maxB[i][j] = INT_MIN

    mask = 1
    firstBit = 1
    for i in range(30):
        for j in range(n):
            aFirst = 0
            bFirst = 0
            if A[j] & firstBit: aFirst = 1
            if B[j] & firstBit: bFirst = 1

            minA[i][aFirst] = min(minA[i][aFirst], A[j] & mask)
            maxA[i][aFirst] = max(maxA[i][aFirst], A[j] & mask)
            minB[i][bFirst] = min(minB[i][bFirst], B[j] & mask)
            minB[i][bFirst] = max(maxB[i][bFirst], B[j] & mask)

        mask = (mask << 1) + 1
        firstBit <<= 1

    result = [1] * 30

    for i in range(30):
        if minA[i][0] != INT_MAX and minB[i][0] != INT_MAX and ((minA[i][0] + minB[i][0]) & firstBit) == 0:
            result[i] = 0

        if maxA[i][1] != INT_MIN and maxB[i][0] != INT_MIN and ((maxA[i][1] + maxB[i][0]) & firstBit) == 0:
            result[i] = 0

        if maxA[i][0] != INT_MIN and maxB[i][1] != INT_MIN and ((maxA[i][0] + maxB[i][1]) & firstBit) == 0:
            result[i] = 0

        if minA[i][1] != INT_MAX and minB[i][1] != INT_MAX and ((minA[i][1] + minB[i][1]) & firstBit) == 0:
            result[i] = 0

        firstBit <<= 1

    ans = 0
    weight = 1
    for i in range(30):
        if result[i]:
            ans += weight
        weight <<= 1

    return ans

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(Solve1(), Solve2())