def todigit(num):
    string = ''
    while num:
        string += str(num % 2)
        num //= 2

    return string[::-1]


def toDec(digit):
    total = 0
    radix = 1
    for i in range(len(digit) - 1, -1, -1):
        total += int(digit[i]) * radix
        radix *= 2
    return total


def AND(d1, d2):
    if len(d1) < len(d2):
        tmp = ['0'] * (len(d2) - len(d1))
        d1 = ''.join(tmp) + d1
    elif len(d1) > len(d2):
        tmp = ['0'] * (len(d1) - len(d2))
        d2 = ''.join(tmp) + d2

    string = ''
    print(d1 ,d2)
    for i in range(len(d1)):
        if d1[i] == '1' and d2[i] == '1':
            string += '1'
        else:
            string += '0'

    return string


def solution(A):
    A.sort()
    n = len(A)
    dp = [1] * len(A)
    for i in range(1, n):
        for j in range(i):
            dec = toDec(AND(todigit(A[i]), todigit(A[j])))
            if dec > 0:
                dp[i] = max(dp[i], dp[j] + 1)
                A[i] = dec
    print(max(dp))

A = [13, 7, 2, 8, 3]
print(solution(A))