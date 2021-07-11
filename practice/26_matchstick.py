# 4
# 3
# 6
# 7
# 15

# https://www.acmicpc.net/problem/3687

for _ in range(int(input())):
    n = int(input())
    start = 2

    dp = [set() for _ in range(n + 1)]

    for i in range(2, n + 1):
        if i == 2:
            dp[2].add(1)
        elif i == 3:
            dp[3].add(7)
        elif i == 4:
            dp[4].add(4)
        elif i == 5:
            dp[5].add(2)
            dp[5].add(5)
            dp[5].add(3)
        elif i == 6:
            dp[6].add(6)
            dp[6].add(9)
            dp[6].add(0)
        elif i == 7:
            dp[7].add(8)

    if n == 2 or n == 3:
        ans = dp[n].pop()
        print(ans, ans)
        continue

    for i in range(4, n + 1):
        for j in range(2, i):
            # for k in range(2, i):
            k = i - j
            if k >= 2:
            # if j + k == i:
                for l in dp[j]:
                    for m in dp[k]:
                        if l != 0:
                            dp[i].add(int(str(l) + str(m)))
                        if m != 0:
                            dp[i].add(int(str(m) + str(l)))

        if i > 7:
            maxvalue = max(dp[i])
            minvalue = min(dp[i])
            dp[i] = set()
            dp[i].add(maxvalue)
            dp[i].add(minvalue)
        #print(dp)

    #print(len(dp[n]))
    if min(dp[n]) == 0:
        dp[n].remove(0)
    print(min(dp[n]), max(dp[n]))
