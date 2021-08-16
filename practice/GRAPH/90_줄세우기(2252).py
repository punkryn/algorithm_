# https://www.acmicpc.net/problem/2252

from sys import stdin
from collections import deque
input = stdin.readline

n, m = map(int, input().split())
students = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    students[b] += 1

q = deque()
# minvalue = min(students[1:])
for idx, i in enumerate(students[1:], start=1):
    if i == 0:
        q.append(idx)

result = []
while q:
    idx = q.popleft()
    result.append(idx)
    for nxt in graph[idx]:
        students[nxt] -= 1
        if students[nxt] == 0:
            q.append(nxt)

for r in result:
    print(r, end=' ')