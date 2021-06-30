# https://programmers.co.kr/learn/courses/30/lessons/60059
import copy

def rotate(key):
    ln_key = len(key)
    newkey = [[0] * ln_key for _ in range(ln_key)]
    for i in range(ln_key):
        for j in range(ln_key):
            newkey[j][ln_key - i - 1] = key[i][j]

    return newkey

def check(matrix, ilock, jlock, len_lock):
    count = True
    for i in range(ilock, ilock + len_lock):
        for j in range(jlock, jlock + len_lock):
            if matrix[i][j] == 2 or matrix[i][j] == 0:
                count = False
    return count

def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    exMatrix = [[0] * (len_lock + (len_key - 1) * 2) for _ in range((len_lock + (len_key - 1) * 2))]
    for i in range(len_lock):
        for j in range(len_lock):
            exMatrix[i + len_key - 1][j + len_key - 1] = lock[i][j]

    len_ex = len(exMatrix)
    for i in range(len_ex - len_key + 1):
        for j in range(len_ex - len_key + 1):
            for _ in range(4):
                tmp = copy.deepcopy(exMatrix)
                for x in range(len_key):
                    for y in range(len_key):
                        tmp[i + x][j + y] += key[x][y]

                if check(tmp, len_key - 1, len_key - 1, len_lock):
                    #print('ans')
                    #show(tmp)
                    return True
                #show(tmp)

                key = rotate(key)

    return False

def show(mat):
    for _ in range(len(mat)):
        print(mat[_])
    print()

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))