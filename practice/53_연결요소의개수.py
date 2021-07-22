# https://www.acmicpc.net/problem/11724

def bfs(start, visited, edges):
    q = []
    visited[start] = 1
    q.append(start)

    while q:
        vertex = q.pop(0)
        for v in edges[vertex]:
            if visited[v] == 0:
                visited[v] = 1
                q.append(v)

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)

visited = [0] * (n + 1)

count = 0
for i in range(1, n + 1):
    if visited[i] == 0:
        count += 1
        bfs(i, visited, edges)

print(count)