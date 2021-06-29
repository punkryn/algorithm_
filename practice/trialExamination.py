# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3#

def solution(answers):
    order1 = [1, 2, 3, 4, 5]
    order2 = [2, 1, 2, 3, 2, 4, 2, 5]
    order3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    result1 = result2 = result3 = 0

    for i, answer in enumerate(answers):
        if answer == order1[i % len(order1)]:
            result1 += 1
        if answer == order2[i % len(order2)]:
            result2 += 1
        if answer == order3[i % len(order3)]:
            result3 += 1

    tmp = []
    maxvalue = max(result1, result2, result3)
    for _ in range(3):
        if maxvalue == result1:
            tmp.append(_ + 1)

    return tmp

answers = [1, 3, 2, 4, 2]
#answers = [1,2,3,4,5]
print(solution(answers))