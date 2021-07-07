# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque
import math

def solution(progresses, speeds):
    answer = []

    q = deque(progresses)
    speeds = deque(speeds)

    start = q.popleft()
    speed = speeds.popleft()
    tmp = 1
    day = math.ceil((100 - start) / speed)
    for i, progress in enumerate(q):
        q[i] = progress + (speeds[i] * day)

    while q:
        p = q.popleft()
        s = speeds.popleft()
        # print(tmp)
        if p >= 100:
            tmp += 1
        else:
            answer.append((tmp))
            tmp = 0
            day = math.ceil((100 - p) / s)
            tmp += 1
            for i, progress in enumerate(q):
                q[i] = progress + (speeds[i] * day)

    answer.append((tmp))
    return answer

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))