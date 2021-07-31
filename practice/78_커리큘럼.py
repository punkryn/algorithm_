# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 10
# 20
# 14
# 18
# 17

from collections import deque

n = int(input())
degree = [0] * (n + 1)
time = [0] * (n + 1)
lecture = [[] for _ in range(n + 1)]
rev = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for idx, j in enumerate(tmp):
        if j == -1:
            break

        if idx == 0:
            time[i] = j
        else:
            lecture[j].append(i)
            rev[i].append(j)
            degree[i] += 1

print(lecture)

result = [0] * (n + 1)

q = deque()

for i in range(1, n + 1):
    if degree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    # result.append(now)
    for i in lecture[now]:
        degree[i] -= 1
        if degree[i] == 0:
            q.append(i)
            result[i] += time[i]
            result[i] += max(result[k] for k in rev[i])
            # for k in rev[i]:
            #     result[i] += result[k]

print(result)