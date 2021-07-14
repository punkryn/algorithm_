def init(c, r):
    global table
    table = [['0'] * (c + 1) for _ in range(r + 1)]

def set(col, row, input_):
    table[row][col] = input_

def update(value_):
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            #print(table[i][j][0])
            if table[i][j][0] not in ['A', 'S', 'M', 'D']:
                value_[i][j] = int(table[i][j])
            else:
                value_[i][j] = case(i, j)
                # op = table[i][j][:3]
                # start = table[i][j][4:6]
                # end = table[i][j][7:9]
                # if op == 'SUM':
                #     v = ADD(start, end)

def ADD(start, end):
    c1 = ord(start[0]) - ord('A') + 1
    r1 = int(start[1])
    c2 = ord(end[0]) - ord('A') + 1
    r2 = int(end[1])

    v1, v2 = 0, 0
    if table[r1][c1][0] in ['A', 'S', 'M', 'D']:
        v1 = case(r1, c1)
    else:
        v1 = int(table[r1][c1])

    if table[r2][c2][0] in ['A', 'S', 'M', 'D']:
        v2 = case(r2, c2)
    else:
        v2 = int(table[r2][c2])

    return v1 + v2

def SUB(start, end):
    c1 = ord(start[0]) - ord('A') + 1
    r1 = int(start[1])
    c2 = ord(end[0]) - ord('A') + 1
    r2 = int(end[1])

    v1, v2 = 0, 0
    if table[r1][c1][0] in ['A', 'S', 'M', 'D']:
        v1 = case(r1, c1)
    else:
        v1 = int(table[r1][c1])

    if table[r2][c2][0] in ['A', 'S', 'M', 'D']:
        v2 = case(r2, c2)
    else:
        v2 = int(table[r2][c2])

    return v1 - v2

def MUL(start, end):
    c1 = ord(start[0]) - ord('A') + 1
    r1 = int(start[1])
    c2 = ord(end[0]) - ord('A') + 1
    r2 = int(end[1])

    v1, v2 = 0, 0
    if table[r1][c1][0] in ['A', 'S', 'M', 'D']:
        v1 = case(r1, c1)
    else:
        v1 = int(table[r1][c1])

    if table[r2][c2][0] in ['A', 'S', 'M', 'D']:
        v2 = case(r2, c2)
    else:
        v2 = int(table[r2][c2])

    return v1 * v2

def DIV(start, end):
    c1 = ord(start[0]) - ord('A') + 1
    r1 = int(start[1])
    c2 = ord(end[0]) - ord('A') + 1
    r2 = int(end[1])

    v1, v2 = 0, 0
    if table[r1][c1][0] in ['A', 'S', 'M', 'D']:
        v1 = case(r1, c1)
    else:
        v1 = int(table[r1][c1])

    if table[r2][c2][0] in ['A', 'S', 'M', 'D']:
        v2 = case(r2, c2)
    else:
        v2 = int(table[r2][c2])

    return v1 // v2

def MAX(start, end):
    c1 = ord(start[0]) - ord('A') + 1
    r1 = int(start[1])
    c2 = ord(end[0]) - ord('A') + 1
    r2 = int(end[1])

    result = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if table[i][j][0] in ['A', 'S', 'M', 'D']:
                if result < case(i, j):
                    result = case(i, j)
            else:
                if result < int(table[i][j]):
                    result = int(table[i][j])

    return result

def MIN(start, end):
    c1 = ord(start[0]) - ord('A') + 1
    r1 = int(start[1])
    c2 = ord(end[0]) - ord('A') + 1
    r2 = int(end[1])

    result = int(1e9)
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if table[i][j][0] in ['A', 'S', 'M', 'D']:
                if result > case(i, j):
                    result = case(i, j)
            else:
                if result > int(table[i][j]):
                    result = int(table[i][j])

    return result

def SUM(start, end):
    c1 = ord(start[0]) - ord('A') + 1
    r1 = int(start[1])
    c2 = ord(end[0]) - ord('A') + 1
    r2 = int(end[1])
    print('sum')
    show(table)
    result = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if table[i][j][0] in ['A', 'S', 'M', 'D']:
                result += case(i, j)
            else:
                result += int(table[i][j])
    return result

def case(r1, c1):
    v1 = 0
    op = table[r1][c1][:3]
    start = table[r1][c1][4:6]
    end = table[r1][c1][7:9]
    if op == 'ADD':
        v1 = ADD(start, end)
    elif op == 'SUB':
        v1 = SUB(start, end)
    elif op == 'MUL':
        v1 = MUL(start, end)
    elif op == 'DIV':
        v1 = DIV(start, end)
    elif op == 'MAX':
        v1 = MAX(start, end)
    elif op == 'MIN':
        v1 = MIN(start, end)
    elif op == 'SUM':
        v1 = SUM(start, end)

    return v1

def show(arr):
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            print(arr[i][j], end=' ')
        print()
    print()

c = 5
r = 5
table = []
value_ = [[0] * (c + 1) for _ in range(r + 1)]

init(c, r)
set(3, 2, '5')
set(5, 2, '13')
set(1, 5, '2')
set(2, 1, '6')
set(1, 1, '-9')
set(3, 4, '9')
set(2, 2, '3')
set(2, 4, '7')
set(5, 3, '2')
set(3, 1, '5')
show(table)

update(value_)
show(value_)

show(table)
set(3, 4, '-9')
set(1, 2, 'SUM(A5,E5)')
set(4, 2, "8")
set(4, 5, "MUL(E2,E3)")
set(2, 2, "SUB(E4,B4)")
set(1, 4, "-9")
set(1, 5, "ADD(C2,A4)")
update(value_)
show(value_)