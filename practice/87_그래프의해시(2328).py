# 4
# 0 0 3 16
# 0 0 9 6
# 3 9 0 0
# 16 6 0 0

# https://www.acmicpc.net/problem/2328

def gcd(a, b):
    if a > b:
        a, b = b, a

    if b % a == 0:
        return a

    return gcd(b % a, a)

def go(edge, cost):
    if edge == 2:
        result.append(cost)
        if len(result) >= 2:
            tmp1 = result.pop()
            tmp2 = result.pop()
            result.append(tmp1 * tmp2 // gcd(tmp1, tmp2))
        return

    for e in graph[edge]:
        edge_, cost_ = e
        if visited[edge_] == 0:
            visited[edge_] = 1
            go(edge_, gcd(cost, cost_))
            visited[edge_] = 0

n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            graph[i + 1].append([j + 1, matrix[i][j]])

# print(graph)

result = []
visited[1] = 1
for tmp in graph[1]:
    edge, cost = tmp
    go(edge, cost)

print(result[0])