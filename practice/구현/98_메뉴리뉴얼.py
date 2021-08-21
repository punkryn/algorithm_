# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations

def solution(orders, course):
    answer = []

    for num in course:
        candidate = {}
        for order in orders:
            for comb in combinations(order, num):
                comb = sorted(comb)
                tmp = ''.join(comb)

                if tmp not in candidate.keys():
                    candidate[tmp] = 1
                else:
                    candidate[tmp] += 1
        maxvalue = 0
        for cand in candidate.keys():
            if candidate[cand] > maxvalue:
                maxvalue = candidate[cand]

        for cand in candidate.keys():
            if maxvalue > 1 and candidate[cand] == maxvalue:
                answer.append(cand)
        # print(candidate)

    answer.sort()
    # print(answer)

    return answer

orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
solution(orders, course)