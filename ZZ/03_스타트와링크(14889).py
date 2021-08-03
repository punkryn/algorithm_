# https://www.acmicpc.net/problem/14889

def total(user):
    result = 0
    for i in range(len(user) - 1):
        for j in range(i + 1, len(user)):
            result += S[user[i]-1][user[j]-1]
            result += S[user[j]-1][user[i]-1]
    return result
flag = False
def go(depth):
    global minvalue
    # global flag
    if depth == n // 2:
        tmp = set(userPool) - set(user)
        #print(user, tmp)
        minvalue = min(minvalue, abs(total((user)) - total(list(tmp))))
        # if minvalue == 0 and not flag:
        #     flag = True
        #     print(user, tmp)
        return

    for i in range(1, n + 1):
        if not user or (not isused[i] and user[-1] < i):
            #print(user, i)
            isused[i] = 1
            user.append(i)
            go(depth + 1)
            user.pop()
            isused[i] = 0

n = int(input())

S = [list(map(int, input().split())) for _ in range(n)]
isused = [0] * (n + 1)
userPool = (list(range(1, n + 1)))
user = []
minvalue = int(1e9)
go(0)
print(minvalue)