# 3
# 1 2 3 4 5
# 6 2 3 4 5
# 7 2 3 4 5
# 8 2 3 4 5
# 9 2 3 4 5
# 2 6 7 8 9
# 3 6 7 8 9
# 4 6 7 8 9
# 5 6 7 8 9

# https://www.acmicpc.net/problem/21608

from sys import stdin

def near(order):
    student, a, b, c, d = order
    tmp = [[0] * (n + 1) for _ in range(n + 1)]
    blank = [[-1] * (n + 1) for _ in range(n + 1)]
    maxvalue = 0
    maxvalue2 = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if classroom[i][j] == 0:
                count = 0
                blankCnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 1 <= nx <= n and 1 <= ny <= n:
                        if classroom[nx][ny] in [a, b, c, d]:
                            #print(nx, ny, classroom[nx][ny], a, b, c, d)
                            count += 1
                        elif classroom[nx][ny] == 0:
                            blankCnt += 1
                tmp[i][j] = count
                blank[i][j] = blankCnt
                maxvalue = max(maxvalue, count)
                maxvalue2 = max(maxvalue2, blankCnt)

    #print(blank)
    result = []
    blanks = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if tmp[i][j] == maxvalue and maxvalue != 0:
                result.append([i, j])
            if blank[i][j] == maxvalue2:
                blanks.append([i, j])
    #print(maxvalue, maxvalue2)
    return result, blanks

def selectPlace(place, blanks, student):
    if len(place) == 0:
        pos = min(blanks, key=lambda x: (x[0], x[1]))
        x, y = pos
        classroom[x][y] = student
    elif len(place) == 1:
        pos = place[0]
        x, y = pos
        classroom[x][y] = student
    else:
        maxCnt = -1
        p = []
        for pla in place:
            x, y = pla
            count = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 1 <= nx <= n and 1 <= ny <= n:
                    if classroom[nx][ny] == 0:
                        count += 1

            if maxCnt < count:
                maxCnt = count
                p.append([maxCnt, x, y])

        tmp = []
        for aa in p:
            if aa[0] == maxCnt:
                tmp.append(aa)
        _, px, py = min(tmp, key=lambda x: (x[1], x[2]))
        classroom[px][py] = student

def makeSum():
    total = 0
    for order in orders:
        student, a, b, c, d = order
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if classroom[i][j] == student:
                    count = 0
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 1 <= nx <= n and 1 <= ny <= n:
                            if classroom[nx][ny] in [a, b, c, d]:
                                count += 1

                    if count == 1:
                        total += 1
                    elif count == 2:
                        total += 10
                    elif count == 3:
                        total += 100
                    elif count == 4:
                        total += 1000
    return total

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

n = int(stdin.readline())
orders = [list(map(int, stdin.readline().split())) for _ in range(n * n)]

classroom = [[0] * (n + 1) for _ in range(n + 1)]

for order in orders:
    student, a, b, c, d = order
    place, blanks = near(order)
    #print(place, student, blanks)
    selectPlace(place, blanks, student)

# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(classroom[i][j], end=' ')
#     print()

total = makeSum()
print(total)