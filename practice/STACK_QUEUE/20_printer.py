# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    answer = 0

    q = []
    for i, priority in enumerate(priorities):
        if i == location:
            q.append([priority, 1])
        else:
            q.append([priority, 0])

    order = 0
    while q:
        p, loc = q.pop(0)
        # flag = True
        # for item in q:
        #     if item[0] > p:
        #         q.append([p, loc])
        #         flag = False
        #         break

        #if flag:
        if all(item[0] <= p for item in q):
            order += 1
            if loc == 1:
                answer = order
                break
        else:
            q.append([p, loc])

    #print(q)

    return answer

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))