# 3
# 3 3 0 1
# 4 2 1 3
# 4 2 2 1

# https://www.acmicpc.net/problem/15685

def dragon_curve():
    standard = vertex[-1]
    for i in range(len(vertex) - 2, -1, -1):
        x, y = vertex[i]
        x_, y_ = standard

        if y == y_:
            vertex.append((x_, y_ + abs(x - x_) if x > x_ else y_ - abs(x - x_)))
        elif x == x_:
            vertex.append((x_ + abs(y - y_) if y < y_ else (x_ - abs(y - y_)), y_))
        elif x != x_ and y != y_:
            if x < x_ and y > y_:
                vertex.append((x_ - abs(y - y_), y_ - abs(x - x_)))
            elif x > x_ and y > y_:
                vertex.append((x_ - abs(y-y_), y_ + abs(x - x_)))
            elif x < x_ and y < y_:
                vertex.append((x_ + abs(y - y_), y_ - abs(x - x_)))
            elif x > x_ and y < y_:
                vertex.append((x_ + abs(y - y_), y_ + abs(x - x_)))

n = int(input())

curves = [list(map(int, input().split())) for _ in range(n)]

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

grid = [[0] * 101 for _ in range(101)]

for curve in curves:
    vertex = []
    x, y, d, g = curve
    vertex.append((x, y))
    vertex.append((x + dx[d], y + dy[d]))

    for _ in range(1, g + 1):
        dragon_curve()
        #print(vertex)

    for v in vertex:
        x1, y1 = v
        if 0 <= x1 <= 100 and 0 <= y1 <= 100:
            grid[x1][y1] = 1

count = 0
for i in range(100):
    for j in range(100):
        if grid[i][j] == 1 and grid[i+1][j] == 1 and grid[i][j+1] == 1 and grid[i+1][j+1] == 1:
            count += 1
#         print(grid[i][j], end=' ')
#     print()
# print()
print(count)