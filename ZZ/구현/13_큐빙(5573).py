# 4
# 1
# L-
# 2
# F+ B+
# 4
# U- D- L+ R+
# 10
# L- U- L+ U- L- U- U- L+ U+ U+

# https://www.acmicpc.net/problem/5373

import copy

def rotate(A):
    if A == 'F':
        tmp = copy.deepcopy(cube[A])
        for i in range(3):
            for j in range(3):
                tmp[j][n-i-1] = cube[A][i][j]
        cube[A] = tmp

        D = copy.deepcopy(cube[2])
        L = copy.deepcopy(cube[1])
        U = copy.deepcopy(cube[5])
        R = copy.deepcopy(cube[3])
        for i in range(3):
            D[2][i] = A[3][2-i][0]
            L[i][2] = A[2][2][i]
            U[2][i] = A[1][2][i]
            R[i][0] = A[5][2][i]


T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    orders = [list(input().split())]

    cube = [
        [['o','o','o'],
         ['o','o','o'],
         ['o','o','o']],
        [['g', 'g', 'g'],
         ['g', 'g', 'g'],
         ['g' ,'g', 'g']],
        [['y', 'y', 'y'],
         ['y', 'y', 'y'],
         ['y', 'y', 'y']],
        [['b','b','b'],
         ['b','b','b'],
         ['b','b','b']],
        [['r','r','r'],
         ['r','r','r'],
         ['r','r','r']],
        [['w','w','w'],
         ['w','w','w'],
         ['w','w','w']]
    ]

