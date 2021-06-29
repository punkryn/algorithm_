# https://programmers.co.kr/learn/courses/30/lessons/42885?language=python3#

def solution(people, limit):
    answer = 0

    people.sort(reverse=True)

    i = 0
    j = len(people) - 1

    while i <= j:
        if people[i] + people[j] > limit:
            answer += 1
            i += 1
        else:
            i += 1
            j -= 1
            answer += 1

    return answer

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))