# 2 20 50
# 50 30
# 20 40

# https://www.acmicpc.net/problem/16234

import sys
sys.setrecursionlimit(100000)

def dfs(population, visited, start, count, unite, num, population_list):
    x, y = start

    if visited[x][y] == 0:
        unite[x][y] = num
        population_list[num][0] += population[x][y]
        population_list[num][1] += 1
        visited[x][y] = 1
    else:
        return

    if count == n * n:
        return
    else:
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if l <= abs(population[x][y] - population[nx][ny]) <= r:
                    dfs(population, visited, [nx, ny], count + 1, unite, num, population_list)

def border_check(population, n, count, unite, population_list):
    num = 0
    for i in range(n):
        for j in range(n):

            dfs(population, visited, [i, j], 1, unite, num, population_list)
            num += 1

    # show(population)
    # show(unite)

def check(unite):
    count = 0
    for i in range(n):
        for j in range(n):
            if unite[i][j] != count:
                return False
            count += 1
    return True

def movement(population, unite, n, population_list):
    for k in range(n * n):
        p = 0
        count = 0
        for i in range(n):
            for j in range(n):
                if unite[i][j] == k:
                    population[i][j] = population_list[k][0] // population_list[k][1]

def show(unite):
    for i in range(n):
        for j in range(n):
            print(unite[i][j], end=' ')
        print()
    print()

n, l, r = map(int, input().split())

population = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
unite = [[-1] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]



count = 0
sw = False
while True:
    population_list = [[0, 0] for _ in range(n * n)]
    border_check(population, n, 0, unite, population_list)
    movement(population, unite, n, population_list)
    #print(population_list)
    sw = check(unite)
    if sw:
        break
    unite = [[-1] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    count += 1


# show(population)
# show(unite)
print(count)