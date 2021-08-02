# https://www.acmicpc.net/problem/13458

from sys import stdin
import math

n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B, C = map(int, stdin.readline().split())

result = n
for a in A:
    if a - B > 0:
        result += math.ceil((a - B)/C)
print(result)