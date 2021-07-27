def bs(left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if r2[mid] > target:
            right = mid - 1
        elif r2[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

def dfs(start):
    global flag1, flag2
    if v2 in vertex[start]:
        flag2 = False
        return v2

    if v1 in vertex[start]:
        flag1 = False
        return v1

    for v in vertex[start]:
        if flag1:
            r1.append(v)
        if flag2:
            r2.append(v)
        dfs(v)
        if flag1:
            r1.pop()
        if flag2:
            r2.pop()

def dfs2(start):
    global total
    total += len(vertex[start])
    for v in vertex[start]:
        dfs2(v)

import sys
sys.stdin = open("./input/ascendent.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    v, e, v1, v2 = map(int, input().split())
    vertex = {}
    for i in range(1, v + 1):
        vertex[i] = []
    ver = list(map(int, input().split()))
    for i in range(0, e * 2, 2):
        vertex[ver[i]].append(ver[i+1])

    #print(vertex)

    r1 = []
    flag1 = True
    r2 = []
    flag2 = True
    dfs(1)

    #print(r1)
    #print(r2)

    flag3 = False
    answer = 1
    for i in range(len(r1) - 1, -1, -1):
        for j in range(len(r2) - 1, -1, -1):
            if r1[i] == r2[j]:
                answer = r1[i]
                flag3 = True
                break
        if flag3:
            break

    total = 1
    dfs2(answer)

    print("#" + str(test_case), answer, total)

