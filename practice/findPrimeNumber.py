# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

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