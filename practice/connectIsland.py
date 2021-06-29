# https://programmers.co.kr/learn/courses/30/lessons/42861?language=python3#

def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])

    parent = [0] * (n + 1)
    for i in range(1, n + 1):
        parent[i] = i

    for cost in costs:
        a, b, c = cost
        if find_parent(parent, a) != find_parent(parent, b):
            union(parent, a, b)
            print(a, b)
            answer += c

    return answer

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
n = 4
print(solution(n, costs))