# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

from collections import deque

def solution(n, computers):
    answer = 0

    network = [-1] * (n)
    visited = [0] * (n)
    for i in range(n):
        next = []
        for j in range(n):
            if i == j:
                continue
            if computers[i][j] == 1:
                next.append((i, j))
        q = deque()
        q.append(next)
        if network[i] == -1:
            network[i] = i
        visited[i] = 1

        while q != deque([[]]):
            next = []
            now = q.popleft()
            print('now', now)
            for item in now:
                for j in range(n):
                    if item[1] == j:
                        continue
                    if computers[item[1]][j] == 1 and visited[item[1]] == 0:
                        network[item[1]] = i
                        next.append((item[1], j))
                        visited[item[1]] = 1

            q.append(next)

    print(network)
    for i in range(n):
        for j in range(n):
            if network[j] == i:
                answer += 1
                break

    return answer

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))