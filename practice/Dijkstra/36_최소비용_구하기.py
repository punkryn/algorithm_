# 5
# 8
# 1 2 2
# 1 3 3
# 1 4 1
# 1 5 10
# 2 4 2
# 3 4 1
# 3 5 1
# 4 5 3
# 1 5

# https://www.acmicpc.net/problem/1916

import heapq
from sys import stdin

n = int(input())
m = int(input())

city = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    city[a].append([c, b])

start, end = map(int, input().split())

table = [int(1e9)] * (n + 1)

table[start] = 0

q = []
heapq.heappush(q, (0, start))

while q:
    #heapq.heapify(q)
    #print(q)
    cost, b = heapq.heappop(q)
    #print(cost, a, b)

    if table[b] < cost:
        continue

    #print(table)
    for item in city[b]:
        tmp = cost + item[0]
        if tmp < table[item[1]]:
            table[item[1]] = tmp
            heapq.heappush(q, (tmp, item[1]))

#print(table)
print(table[end])