# https://programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    answer = 0

    visited = [0] * len(words)
    q = deque()
    for i, case in nextCase(begin, words, visited):
        q.append([case, 1, i])
    # visited[case[0][2]] = 1
    # q.append(case)

    while q:
        #print(visited, q)
        now = q.popleft()
        #print('now', now)
        crt_word, stage, index = now
        #print(crt_word, stage, index)
        visited[index] = 1
        if crt_word == target:
            answer = stage
            break

        for i, case in nextCase(crt_word, words, visited):
            q.append([case, stage + 1, i])

    return answer

def nextCase(begin, words, visited):
    n = len(begin)
    tmp = []
    for i, word in enumerate(words):
        count = 0
        for j in range(n):
            if begin[j] != word[j]:
                count += 1

        if count == 1 and visited[i] == 0:
            tmp.append([i, word])
    return tmp

begin = 'hit'
target = 'cog'
words = ["hot", "dot", "dog", "lot", "log"]
print(solution(begin, target, words))