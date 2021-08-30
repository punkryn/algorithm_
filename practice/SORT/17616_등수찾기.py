# https://www.acmicpc.net/problem/17616

from sys import stdin
from collections import deque
input = stdin.readline

def bfs(x, graph):
    rank = 0
    q = deque()
    q.append(x)
    visited[x] = True

    while q:
        # print(q)
        v = q.popleft()
        for nv in graph[v]:
            if not visited[nv]:
                q.append(nv)
                visited[nv] = True
                rank += 1

    return rank

n, m, x = map(int, input().split())

lower = [[] for _ in range(n + 1)]
higher = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b= map(int, input().split())
    higher[a].append(b)
    lower[b].append(a)

print(1 + bfs(x, lower), n - bfs(x, higher))

# for _ in range(m):
#     a, b = map(int, input().split())
#     if student[b] == -1:
#         student[b] = 0
#     if student[a] == -1:
#         student[a] = 0
#
#     student[b] += 1
#     graph[a].append(b)
#
# if student[x] == -1:
#     print(1, n)
# else:
#     q = deque()
#
#     start = 1
#     end = 0
#     team = 1
#     for i in range(1, len(student)):
#         if student[i] == 0:
#             end += 1
#             q.append((i, end, team))
#
#     left = 1
#     right = 0
#     flag = False
#     flag2 = True
#     while q:
#         # print(q)
#         n, rank, t = q.popleft()
#
#         if not flag and n == x:
#             left = rank
#             right= left - 1
#             team = t
#             flag = True
#             flag2 = False
#
#         if team == t and flag2:
#             flag2 = False
#
#         if flag and not flag2:
#             if team == t:
#                 right += 1
#             else:
#                 # left += right
#                 break
#
#         for num in graph[n]:
#             student[num] -= 1
#             if student[num] == 0:
#                 if num == x:
#                     left = rank + 1
#                     right = left - 1
#                     team = t + 1
#                     flag = True
#                 q.append((num, rank + 1, t + 1))
#
#     print(left, right)