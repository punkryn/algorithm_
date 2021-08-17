# https://programmers.co.kr/learn/courses/30/lessons/81304

from collections import deque
import copy

def solution(n, start, end, roads, traps):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    graph2 = [[] for _ in range(n + 1)]
    for road in roads:
        a, b, c = road
        graph[a].append([a, b, c])
        graph2[b].append([a, b, c])

    q = deque()
    for road in graph[start]:
        q.append(road)
    visited = [0] * (n + 1)
    trap_position = [0] * (n + 1)
    for trap in traps:
        trap_position[trap] = 1

    if visited[start] == 0 and trap_position[start] != 1:
        visited[start] = 1
    # print(q)
    #print(graph)
    #print(graph2)
    while q:
        pre, now, cost = q.popleft()
        #print(pre, now)
        if end == now:
            answer = cost
            break

        if visited[now] == 0 and trap_position[now] != 1:
            visited[now] = 1

        _graph2 = copy.deepcopy(graph2)
        _graph = copy.deepcopy(graph)
        if trap_position[now] == 1:
            for g in graph2[now]:
                a, b, c = g
                _graph[a].remove([a, b, c])
                _graph[b].append([b, a, c])
                _graph2[now].remove([a, b, c])
                _graph2[a].append([b, a, c])

            #print(graph)
            #print(graph2)

            for g in graph[now]:
                a, b, c = g
                _graph[a].remove([a, b, c])
                _graph[b].append([b, a, c])
                _graph2[b].remove([a, b, c])
                _graph2[a].append([b, a, c])

            graph = _graph
            graph2 = _graph2

        #print(graph2)
        #print(graph)
        #print(visited)
        for g in graph[now]:
            a, b, c = g
            if visited[b] == 0:
                q.append([a, b, cost + c])

    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))