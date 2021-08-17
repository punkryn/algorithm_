n = int(input())

index = 0
num = [0] * n
num[0] = 1
n1, n2, n3 = 2, 3, 5
i2 = i3 = i5 = 0
for i in range(1, n):
    num[i] = min(n1, n2, n3)

    if num[i] == n1:
        i2 += 1
        n1 = num[i2] * 2

    if num[i] == n2:
        i3 += 1
        n2 = num[i3] * 3

    if num[i] == n3:
        i5 += 1
        n3 = num[i5] * 5

print(num)
print(num[n - 1])