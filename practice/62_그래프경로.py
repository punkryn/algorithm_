# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg&&#

from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)

    s, g = map(int, input().split())

    visited = [0] * (v + 1)

    q = deque()
    q.append(s)

    flag = 0
    while q:
        now = q.popleft()
        visited[now] = 1

        if now == g:
            flag = 1
            break

        for nxt in graph[now]:
            if visited[nxt] == 0:
                q.append(nxt)

    print("#" + str(test_case), flag)