# https://www.acmicpc.net/problem/15686

# 5 3
# 0 0 1 0 0
# 0 0 2 0 1
# 0 1 2 0 0
# 0 0 1 0 0
# 0 0 0 0 2

from itertools import combinations

n, m = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(n)]

chickens = []
houses = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chickens.append([i, j])
        elif city[i][j] == 1:
            houses.append([i, j])

result = int(1e9)
for chicken in combinations(chickens, m):
    distance = 0
    for house in houses:
        distance += min(abs(house[0] - pos[0]) + abs(house[1] - pos[1]) for pos in chicken)

    if result > distance:
        result = distance
print(result)