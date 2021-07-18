# https://www.acmicpc.net/contest/problem/658/3

from collections import deque
from sys import stdin

n, t, w = map(int, input().split())

q = deque()
for _ in range(n):
    q.append(list(map(int, stdin.readline().split())))

m = int(stdin.readline())
nxt = deque()
for _ in range(m):
    nxt.append(list(map(int, stdin.readline().split())))
nxt = sorted(nxt, key=lambda x: x[2])
nxt = deque(nxt)

time = 0
time_count = 0
while q and time < w:
    now = q[0]
    flag = False
    flag2 = False
    if len(now) == 2:
        px, tx = now
        flag = True
    elif len(now) == 3:
        px, tx, cx = now
        flag2 = True

    print(px)

    if tx > t:
        time += 1
        time_count += 1

        if nxt and time == nxt[0][2]:
            q.append(nxt.popleft())

        if time_count == t:
            time_count = 0
            tx -= t
            # if time == nxt[0][2]:
            #     q.append(nxt.popleft())

            q.popleft()
            if flag:
                q.append([px, tx])
            if flag2:
                q.append([px, tx, cx])
    else:
        time += 1
        # tx = 0
        time_count += 1

        if time_count == tx:
            q.popleft()
            time_count = 0

        if nxt and time == nxt[0][2]:
            q.append(nxt.popleft())

    #print(q)