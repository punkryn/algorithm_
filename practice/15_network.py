# https://programmers.co.kr/learn/courses/30/lessons/43162?language=python3

from collections import deque

def solution(n, computers):
    answer = 0

    visited = [0] * n

    def next(computers, n):
        tmp = []
        for i in range(len(computers)):
            if computers[n][i] == 1:
                tmp.append(i)
        return tmp

    for i in range(n):
        if visited[i] == 0:
            answer += 1
            q = deque()
            visited[i] = 1
            for nex in (next(computers, i)):
                q.append(nex)
            while q:
                #print(q)
                ne = q.popleft()
                #print(ne) # 0 1
                if visited[ne] == 0:
                    visited[ne] = 1
                    for nex in next(computers, ne):
                        q.append(nex)

    return answer



n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))