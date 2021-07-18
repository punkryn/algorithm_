# https://www.acmicpc.net/contest/problem/658/4

from sys import stdin

n, m = map(int, input().split())
ball = [list(map(int, stdin.readline().split())) for _ in range(n)]
gun = [list(map(int, stdin.readline().split())) for _ in range(m)]

bias = {}
for b in ball:
    x, y, hp = b
    if x != 0:
        if y != 0:
            t = y / x
        else:
            t = 'hor'
    else:
        t = 'ver'

    if t not in bias.keys():
        bias[t] = {}
        if t == 'hor':
            bias[t][7] = [] # 우
            bias[t][8] = [] # 좌
        elif t == 'ver':
            bias[t][5] = [] # 위
            bias[t][6] = [] # 아래
        else:
            bias[t][1] = []
            bias[t][2] = []
            bias[t][3] = []
            bias[t][4] = []


    if x > 0 and y > 0:
        bias[t][1].append(hp)
    elif x < 0 and y > 0:
        bias[t][2].append(hp)
    elif x < 0 and y < 0:
        bias[t][3].append(hp)
    elif x > 0 and y < 0:
        bias[t][4].append(hp)
    elif x == 0 and y > 0:
        bias[t][5].append(hp)
    elif x == 0 and y < 0:
        bias[t][6].append(hp)
    elif y == 0 and x > 0:
        bias[t][7].append(hp)
    elif y == 0 and x < 0:
        bias[t][8].append(hp)


#print(bias)

for g in gun:
    x, y, d = g
    if x != 0:
        if y != 0:
            t = y / x
        else:
            t = 'hor'
    else:
        t = 'ver'

    #if t in bias.keys():
    try:
        if x > 0 and y > 0:
            for i in range(len(bias[t][1])):
                bias[t][1][i] -= d
        elif x < 0 and y > 0:
            for i in range(len(bias[t][2])):
                bias[t][2][i] -= d
        elif x < 0 and y < 0:
            for i in range(len(bias[t][3])):
                bias[t][3][i] -= d
        elif x > 0 and y < 0:
            for i in range(len(bias[t][4])):
                bias[t][4][i] -= d
        elif x == 0 and y > 0:
            for i in range(len(bias[t][5])):
                bias[t][5][i] -= d
        elif x == 0 and y < 0:
            for i in range(len(bias[t][6])):
                bias[t][6][i] -= d
        elif y == 0 and x > 0:
            for i in range(len(bias[t][7])):
                bias[t][7][i] -= d
        elif y == 0 and x < 0:
            for i in range(len(bias[t][8])):
                bias[t][8][i] -= d
    except(KeyError):
        continue


# print(bias)

count = 0
for key in bias.keys():
    #print(key)
    for k in bias[key].keys():
        for i in bias[key][k]:
            if i > 0:
                count += 1
print(count)