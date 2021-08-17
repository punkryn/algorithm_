# https://programmers.co.kr/learn/courses/30/lessons/81304

import copy

result = 0

def dfs(start, end, cost, graph, graph2, trap_position, visited):
    global result
    # print(start, cost, end)
    # print(graph)
    # print(graph2)

    if start == end:
        result = cost
        return

    visited_ = copy.deepcopy(visited)

    _graph = copy.deepcopy(graph)
    _graph2 = copy.deepcopy(graph2)

    if trap_position[start] == 1:
        for g in graph2[start]:
            a, b, c = g
            _graph[a].remove([a, b, c])
            _graph[b].append([b, a, c])
            _graph2[start].remove([a, b, c])
            _graph2[a].append([b, a, c])

        #print(graph)
        #print(graph2)

        for g in graph[start]:
            a, b, c = g
            _graph[a].remove([a, b, c])
            _graph[b].append([b, a, c])
            _graph2[b].remove([a, b, c])
            _graph2[a].append([b, a, c])

        #print(_graph)
        #print(_graph2)

    for road in _graph[start]:
        a, b, c = road
        #print(a, b, c)
        if visited_[start] == 0 or trap_position[start] == 1:
            visited_[start] += 1
        #print(visited_)
        if visited_[b] == 0 or (visited_[b] > 0 and visited_[b] >= visited_[a] and trap_position[a] == 1 and trap_position[b] == 1):
            dfs(b, end, cost + c, _graph, _graph2, trap_position, visited_)

def solution(n, start, end, roads, traps):
    global result
    answer = 0

    graph = [[] for _ in range(n + 1)]
    graph2 = [[] for _ in range(n + 1)]
    for road in roads:
        a, b, c = road
        graph[a].append([a, b, c])
        graph2[b].append([a, b, c])

    visited = [0] * (n + 1)
    trap_position = [0] * (n + 1)
    for trap in traps:
        trap_position[trap] = 1

    dfs(start, end, 0, graph, graph2, trap_position, visited)

    answer = result

    return answer

n = 4
start = 1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]
traps = [2, 3]
print(solution(n, start, end, roads, traps))