# https://programmers.co.kr/learn/courses/30/lessons/42626
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

import heapq

def solution(scoville, K):
    answer = 0

    # heapq.heapify(scoville)
    scoville.sort()
    flag = False
    flag2 = False
    while True:
        #print(scoville)
        if len(scoville) >= 2:
            s1 = heapq.heappop(scoville)
            s2 = heapq.heappop(scoville)
        elif len(scoville) == 1:
            s1 = heapq.heappop(scoville)
            flag = True
        else:
            flag2 = True
            break

        if s1 >= K:
            break

        if not flag:
            heapq.heappush(scoville, s1 + s2 * 2)
            answer += 1
    #print(scoville)
    if flag2:
        answer = -1
    return answer

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))