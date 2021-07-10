# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0

    n = len(citations)
    if n == 1:
        answer = 1 if citations[0] > 0 else 0
        return answer
    citations.sort(reverse=True)
    max_value = citations[0]

    tmp = n + 1

    if citations[0] == 0:
        return 0

    for h in range(1, n):
        #if len(citations[:h+1]) >= h and h + 1 < n and citations[h + 1] <= h:
        if citations[h - 1] >= h and citations[h] <= h:
            tmp = h
            answer = h
            return answer

    if len(citations) == n:
        answer = n

    return answer

#citations = [7]
citations = [0, 0]
print(solution(citations))