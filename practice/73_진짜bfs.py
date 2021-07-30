# 3
# 4
# 1 1 2
# 4
# 1 1 3
# 11
# 1 1 3 3 2 4 1 3 2 9
#import sys
import heapq
from collections import deque
#sys.stdin = open("input.txt", "r")

def bfs(start, depth):
    # if tree[start] == []:
    #     return
    #
    # for i in tree[start]:
    #     #toRoot(i, depthlist[i])
    #     depthlist[i] = (depth + 1)
    #     dfs(i, depth + 1)

    q = deque()
    q.append([start, depth])
    depthlist[start] = depth

    while q:
        now, d = q.popleft()
        for i in tree[now]:
            depthlist[i] = d + 1
            q.append([i, d + 1])

def lca(prev, now):
    anc1 = depthlist[prev]
    anc2 = depthlist[now]

    gap = abs((anc1) - (anc2))
    #print(prev, now, anc1, anc2)

    count = 0
    if anc1 > anc2:
        while anc1 != anc2:
            prev = rev[prev]
            anc1 -= 1
            count += 1
    elif anc1 < anc2:
        while anc1 != anc2:
            now = rev[now]
            anc2 -= 1
            count += 1

    while prev != now:
        prev = rev[prev]
        now = rev[now]
        count += 2

    #print(count)
    return count

T = int(input())
MAX = int(1e5) + 1
for test_case in range(1, T + 1):
    n = int(input())
    tree = [[] for _ in range(MAX)]
    rev = [0] * (MAX)
    for i, node in enumerate(map(int, input().split()), start=2):
        #heapq.heappush(tree[node], i)
        tree[node].append(i)
        rev[i] = node

    for g in tree:
        g.sort()

    depthlist = [0] * (MAX)
    bfs(1, 0)
    #print(depthlist)
    # print(tree)
    # print(rev)

    total = 0

    q = deque()
    q.append(1)

    prev = 0
    while q:
        now = q.popleft()
        if now != 1:
            anc = lca(prev, now)
            total += anc

        #while tree[now]:
            #tmp = heapq.heappop(tree[now])
        for tmp in tree[now]:
            q.append(tmp)
        prev = now
    print("#" + str(test_case), total)