# 60466175 36

# https://www.acmicpc.net/problem/11005

n, b = map(int, input().split())

alphabet = {}
start = 'A'
for i in range(10):
    alphabet[i] = str(i)
for _ in range(26):
    alphabet[ord(start) - 55] = start
    start = chr(ord(start) + 1)

# print(alphabet)

answer = ''
while n:
    target = n % b
    answer += alphabet[target]

    n //= b

print(answer[::-1])