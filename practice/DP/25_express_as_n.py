# https://programmers.co.kr/learn/courses/30/lessons/42895?language=python3

def solution(N, number):
    answer = -1

    if N == number:
        return 1

    union = [set() for _ in range(8)]
    tmp = ''
    for i in range(8):
        tmp += str(N)
        union[i].add(int(tmp))
        print(union)
        for j in range(i):
            for k in union[j]:
                for l in union[i - j - 1]:
                    union[i].add(k + l)
                    union[i].add(k - l)
                    union[i].add(k * l)
                    if l != 0:
                        union[i].add(k // l)

        for num in union[i]:
            if num == number:
                print(union)
                answer = i + 1
                return answer
    return answer

n = 5
number = 12
print(solution(n, number))