# 1
# 5
# 2
# 2 5
# 6 10

# 1
# 15
# 7
# 2 5
# 6 10
# 12 13
# 15 16
# 20 25
# 26 27
# 28 29

# import sys
# sys.stdin = open("./input/time.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    l = int(input())
    n = int(input())

    s = [0] * (n + 1)
    a = [0] * n
    b = [0] * n

    for i in range(n):
        a_, b_ = map(int, input().split())
        a[i] = a_
        b[i] = b_
        s[i + 1] = s[i] + (b_ - a_)

    s_ = 0
    ans = 0
    for e in range(n):
        while s_ <= e and a[s_] + l <= b[e]:
            length = a[s_] + l - a[e]
            if length >= 0:
                ans = max(ans, s[e] - s[s_] + length)
            else:
                ans = max(ans, s[e] - s[s_])

            s_ += 1

    if s_ < n:
        ans = max(ans, s[n] - s[s_])

    print("#" + str(test_case), ans)