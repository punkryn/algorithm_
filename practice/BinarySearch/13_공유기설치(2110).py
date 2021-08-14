# https://www.acmicpc.net/problem/2110

def install(mid):
    idx = 0
    count = 1
    idx2 = idx + 1
    while idx < len(houses) - 1 and idx2 < len(houses) and count < c:
        gap = houses[idx2] - houses[idx]
        if gap >= mid:
            count += 1
            idx = idx2
            idx2 = idx + 1
        else:
            idx2 += 1

    if count == c:
        return True
    else:
        return False

n, c = map(int, input().split())

houses = [int(input()) for _ in range(n)]

left = 1
right = int(1e9)

houses.sort()

while left <= right:
    mid = (left + right) // 2
    if install(mid):
        left = mid + 1
    else:
        right = mid - 1
    # print(left, right)

print(right)