# https://programmers.co.kr/learn/courses/30/lessons/42862

import copy

def solution(n, lost, reserve):
    answer = 0

    student = [1] * (n + 1)

    for i in lost:
        student[i] = 0

    tmp = copy.deepcopy(reserve)
    for i in reserve:
        if student[i] == 0:
            student[i] = 1
            tmp.remove(i)

    for i in tmp:
        flag = False
        if i - 1 >= 1 and student[i - 1] == 0:
            flag = True
            student[i - 1] = 1

        if not flag and i + 1 <= n and student[i + 1] == 0:
            student[i + 1] = 1

    for i in range(1, n + 1):
        if student[i] == 1:
            answer += 1

    # print(student)
    return answer

n = 5
lost = [1,2,3,4]
reserve = [1,4]
print(solution(n, lost, reserve))