# https://programmers.co.kr/learn/courses/30/lessons/42894

def solution(board):
    answer = 0

    n = len(board)
    block_count = 0

    # for i in range(len(board)):
    #     print(board[i])

    blocks = [[] for _ in range(201)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0:
                blocks[board[i][j]].append((i, j))
                if block_count < board[i][j]:
                    block_count = board[i][j]

    position = [[] for _ in range(block_count + 1)]
    blank = [[] for _ in range(block_count + 1)]

    for i, block in enumerate(blocks[:block_count+1]):
        if block == []:
            continue

        block.sort()

        x1 = block[0][0]
        x2 = block[-1][0]

        block.sort(key=lambda x: x[1])
        y1 = block[0][1]
        y2 = block[-1][1]

        position[i].append((x1, y1))
        position[i].append((x2, y2))

    # print(position)

    for i, pos in enumerate(position[1:], start=1):
        if pos == []:
            continue
        left, right = pos
        x1, y1 = left
        x2, y2 = right

        for j in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                if board[j][k] != i:
                    blank[i].append((j, k))

    #print(blank)

    #q = [idx for idx in isOpen(blank, board)]
    q = []
    iop = isOpen(blank, board, n)
    for idx in iop:
        q.append(idx)

    visited = [0] * (block_count + 1)
    while q:
        #print('q', q)

        idx = q.pop(0)

        if visited[idx] == 1:
            continue

        visited[idx] = 1

        #print('idx', idx)
        blank[idx] = []
        #print(blank)
        pos = position[idx]
        if pos == []:
            continue
        left, right = pos
        x1, y1 = left
        x2, y2 = right

        for j in range(x1, x2 + 1):
            for k in range(y1, y2 + 1):
                board[j][k] = 0

        # for aa in range(n):
        #     print(board[aa])

        answer += 1

        position[idx] = []
        # print(position)

        for idx in isOpen(blank, board, n):
            if visited[idx] == 0:
                q.append(idx)

    return answer

def isOpen(blank, board, n):
    ans = []

    for i, b in enumerate(blank[1:], start=1):
        if b == []:
            continue

        flag = True
        flag2 = True

        first = b[0][0]
        firsty = b[0][1]

        second = b[1][0]
        secondy = b[1][1]

        # print(first, firsty, second, secondy)

        while first >= 0:
            if board[first][firsty] != 0:
                flag = False
                break
            first -= 1

        while second >= 0:
            if board[second][secondy] != 0:
                flag2 = False
                break
            second -= 1

        if flag and flag2:
            #print('i', i)
            ans.append(i)

    return ans


board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
#board = [[1, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
board = [[3, 0, 0, 0], [3, 3, 3, 2], [5, 2, 2, 2], [5, 5, 5, 0]]
print(solution(board))