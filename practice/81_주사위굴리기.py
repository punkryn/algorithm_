# 4 2 0 0 8
# 0 2
# 3 4
# 5 6
# 7 8
# 4 4 4 1 3 3 3 2

# https://www.acmicpc.net/problem/14499

import copy

def rotate(d):
    dice_ = copy.deepcopy(dice)
    if d == 4:
        dice[0] = dice_[3]
        dice[1] = dice_[0]
        dice[3] = dice_[5]
        dice[5] = dice_[1]
        #print('4', dice)
    elif d == 3:
        dice[0] = dice_[1]
        dice[1] = dice_[5]
        dice[3] = dice_[0]
        dice[5] = dice_[3]
        #print('3', dice)
    elif d == 2:
        dice[0] = dice_[4]
        dice[2] = dice_[0]
        dice[4] = dice_[5]
        dice[5] = dice_[2]
        #print('2', dice)
    else:
        dice[0] = dice_[2]
        dice[2] = dice_[5]
        dice[4] = dice_[0]
        dice[5] = dice_[4]
        #print('1', dice)


n, m, x, y, k = map(int, input().split())
_map = [list(map(int, input().split())) for _ in range(n)]
operation = list(map(int, input().split()))

dx = [100, 0, 0, -1, 1]
dy = [100, 1, -1, 0, 0]

dice = [1, 2, 3, 5, 4, 6]
diceVal = [0] * 7

for op in operation:
    nx = x + dx[op]
    ny = y + dy[op]

    if 0 <= nx < n and 0 <= ny < m:
        rotate(op)
        if _map[nx][ny] == 0:
            _map[nx][ny] = diceVal[dice[0]]
        else:
            diceVal[dice[0]] = _map[nx][ny]
            _map[nx][ny] = 0

        x = nx
        y = ny
        print(diceVal[dice[-1]])

