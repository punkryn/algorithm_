# https://www.acmicpc.net/problem/14888

def go(depth, total):
    global maxvalue
    global minvalue
    if depth == n:
        if maxvalue < total:
            maxvalue = total
        if minvalue > total:
            minvalue = total
        return

    if op[0] > 0:
        op[0] -= 1
        go(depth + 1, total + A[depth])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        go(depth + 1, total - A[depth])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        go(depth + 1, total * A[depth])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        if total < 0:
            total = -total
            total //= A[depth]
            total = -total
            go(depth + 1, total)
        else:
            go(depth + 1, total // A[depth])
        op[3] += 1

n = int(input())
A = list(map(int, input().split()))
op = list(map(int, input().split()))

maxvalue = -int(1e9)
minvalue = int(1e9)
go(1, A[0])
print(maxvalue)
print(minvalue)