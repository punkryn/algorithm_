# https://programmers.co.kr/learn/courses/30/lessons/42842?language=python3

def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0 and i <= yellow // i:
            hei = i
            width = yellow // i
            if brown == (hei * 2 + width * 2 + 4):
                answer.append(width + 2)
                answer.append(hei + 2)
                break
    return answer

brown = 24
yellow = 24
print(solution(brown, yellow))