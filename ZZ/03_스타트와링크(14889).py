# https://www.acmicpc.net/problem/14889

def total(user):
    result = 0
    for i in range(len(user) - 1):
        for j in range(1, len(user)):
            result += S[user[i]-1][user[j]-1]
            result += S[user[j]-1][user[i]-1]
    return result

def go(depth):
    global minvalue
    if depth == n // 2:
        tmp = userPool - user
        print(user, tmp)
        minvalue = min(minvalue, abs(total(list(user)) - total(list(tmp))))
        return

    for i in range(1, n + 1):
        if not isused[i]:
            isused[i] = 1
            user.add(i)
            go(depth + 1)
            user.remove(i)
            isused[i] = 0

n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]
isused = [0] * (n + 1)
userPool = set(list(range(1, n + 1)))
user = set()
minvalue = int(1e9)
go(0)
print(minvalue)