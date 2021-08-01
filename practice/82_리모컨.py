# 5457
# 3
# 6 7 8

# https://www.acmicpc.net/problem/1107

n = int(input())
m = int(input())
nums = {str(i) for i in range(10)}
if m > 0:
    nums -= set(map(str, input().split()))

min_cnt = abs(100 - n)
for num in range(1000001):
    num = str(num)
    for j in range(len(num)):
        if num[j] not in nums:
            break
        elif j == len(num) - 1:
            min_cnt = min(min_cnt, abs(n - int(num)) + len(str(num)))

print(min_cnt)