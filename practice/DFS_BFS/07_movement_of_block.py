# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def solution(board):
    answer = 0
    length = len(board)
    start = [[0, 0], [0, 1]]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    Rx = [-1, 1, -1, 1]
    Ry = [-1, -1, 1, 1]

    q = deque()

    time = 0
    q.append([[[0, 0], [0, 1]], time])
    visited = [{(0, 0), (0, 1)}]
    while q:
        start, time = q.popleft()
        left, right = start
        lx, ly = left
        rx, ry = right

        #print(left, right)

        if (lx == length - 1 and ly == length - 1) or (rx == length - 1 and ry == length -1):
            answer = time
            break

        for i in range(4):
            lnx = lx + dx[i]
            lny = ly + dy[i]
            rnx = rx + dx[i]
            rny = ry + dy[i]

            if 0 <= lnx < length and 0 <= lny < length and 0 <= rnx < length and 0 <= rny < length:
                if [(lnx, lny), (rnx, rny)] not in visited:
                    visited.append({(lnx, lny), (rnx, rny)})
                    q.append([[[lnx, lny], [rnx, rny]], time + 1])

        if lx == rx:
            for i in range(2):
                lnx = lx
                lny = ly
                rnx = rx + Rx[i]
                rny = ry + Ry[i]

                if 0 <= lnx < length and 0 <= lny < length and 0 <= rnx < length and 0 <= rny < length:
                    if (i == 0 and board[rx - 1][ry] == 0) or (i == 1 and board[rx + 1][ry] == 0):
                        if [(lnx, lny), (rnx, rny)] not in visited:
                            visited.append({(lnx, lny), (rnx, rny)})
                            q.append([[[lnx, lny], [rnx, rny]], time + 1])

            for i in range(2, 4):
                lnx = lx + Rx[i]
                lny = ly + Ry[i]
                rnx = rx
                rny = ry

                if 0 <= lnx < length and 0 <= lny < length and 0 <= rnx < length and 0 <= rny < length:
                    if (i == 2 and board[lx - 1][ly] == 0) or (i == 3 and board[lx + 1][ly] == 0):
                        if [(lnx, lny), (rnx, rny)] not in visited:
                            visited.append({(lnx, lny), (rnx, rny)})
                            q.append([[[lnx, lny], [rnx, rny]], time + 1])
        elif ly == ry:
            for i in [-1, 1]:
                lnx = lx + 1
                lny = ly +i
                rnx = rx
                rny = ry

                if 0 <= lnx < length and 0 <= lny < length and 0 <= rnx < length and 0 <= rny < length:
                    if (i == -1 and board[lx][ly - 1] == 0) or (i == 1 and board[lx][ly + 1] == 0):
                        if board[lnx][lny] == 0 and board[rnx][rny] == 0:
                            if [(lnx, lny), (rnx, rny)] not in visited:
                                visited.append({(lnx, lny), (rnx, rny)})
                                q.append([[[lnx, lny], [rnx, rny]], time + 1])

            for i in [-1, 1]:
                lnx = lx
                lny = ly
                rnx = rx - 1
                rny = ry + i

                if 0 <= lnx < length and 0 <= lny < length and 0 <= rnx < length and 0 <= rny < length:
                    if (i == -1 and board[rx][ry - 1] == 0) or (i == 1 and board[rx][ry + 1] == 0):
                        if board[lnx][lny] == 0 and board[rnx][rny] == 0:
                            if [(lnx, lny), (rnx, rny)] not in visited:
                                visited.append({(lnx, lny), (rnx, rny)})
                                q.append([[[lnx, lny], [rnx, rny]], time + 1])


    return answer

def check(x1, y1, x2, y2, n):
    if (x1 == n - 1 and y1 == n - 1) or (x2 == n - 1 and y2 == n - 1):
        return True
    return False

def show(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=' ')
        print()
    print()

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
print(solution(board))