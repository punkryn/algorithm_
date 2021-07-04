# 5 3
# 1
# 2
# 8
# 4
# 9

#https://www.acmicpc.net/problem/2110

from sys import stdin

n, c = map(int, stdin.readline().split())
houses = [int(stdin.readline()) for _ in range(n)]

houses = sorted(houses)
# print(houses)

start = 1
end = houses[-1] - houses[0]
result = 0

while start <= end:
    mid = (start + end) // 2

    value = houses[0]
    count = 1

    for i in range(1, n):
        if houses[i] >= value + mid:
            count += 1
            value = houses[i]

    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)