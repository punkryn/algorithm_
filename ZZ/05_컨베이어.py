# https://www.acmicpc.net/problem/20055

from collections import deque

def rotate():
    A.insert(0, A.pop())
    if robots and robots[0] + 1 == n - 1:
        tmp = robots.popleft()
        onRobot[tmp] = 0
        onRobot[tmp + 1] = 0
    onRobot.insert(0, onRobot.pop())
    for i, robot in enumerate(robots):
        robots[i] += 1

def move_robot():
    if robots and robots[0] + 1 == n - 1 and A[robots[0] + 1] >= 1:
        A[robots[0] + 1] -= 1
        onRobot[robots[0]] = 0
        robots.popleft()

    for i, robot in enumerate(robots):
        if onRobot[robot + 1] == 0 and A[robot + 1] >= 1:
            onRobot[robot] = 0
            robots[i] += 1
            A[robot + 1] -= 1
            onRobot[robot + 1] = 1

def on_robot():
    if A[0] > 0:
        onRobot[0] = 1
        A[0] -= 1
        robots.append(0)

def check():
    brokenCnt = 0
    for i in A:
        if i == 0:
            brokenCnt += 1
    return brokenCnt

n, k = map(int, input().split())
A = list(map(int, input().split()))

stage = 1
onRobot = [0] * n
robots = deque()
brokenCnt = 0
for i in A:
    if i == 0:
        brokenCnt += 1

while brokenCnt < k:
    rotate()
    move_robot()
    on_robot()
    brokenCnt = check()
    if brokenCnt < k:
        stage += 1

print(stage)