# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

# 처음 접근은 7자리까지의 소수를 모두 구하고 해당 조합이 소수인지 아닌지 판별하는 방법을 생각하였다.
# 시간초과가 발생하여 접근방법을 바꿔야할 필요가 있었다.
# 모든 소수를 구해놓지 않고 각 조합이 소수인지 아닌지 판별하는 방식으로 하였다.
# 판별법은 에라토스테네스의 판별법
# 해당 숫자의 제곱근까지만 검사하면 된다는 것이다.

from itertools import permutations
import math

def solution(numbers):
    answer = 0

    tmp = set()
    for length in range(1, len(numbers) + 1):
        comb = permutations(numbers, length)
        for item in comb:
            #print('item', item)
            number = int(''.join(item))
            #print(number)
            tmp.add(number)

    # print(tmp)
    for num in tmp:
        if num <= 1:
            continue
        if isPrime(num):
            print(num)
            answer += 1

    return answer

def isPrime(number):
    # if number % 2 == 0:
    #     return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

# def makePrime():
#     result = [2]
#
#     num = 3
#     while num < 1000:
#         for i, n in enumerate(result):
#             if num % n == 0:
#                 break
#             else:
#                 if i == len(result) - 1:
#                     result.append(num)
#
#         num += 2
#     return result

numbers = "011"
#primeNumber = makePrime()
print(solution(numbers))