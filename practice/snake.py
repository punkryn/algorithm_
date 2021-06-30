# https://www.acmicpc.net/problem/3190

# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

def simulation(room, apple_position, direct):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    time = 0
    d = 0
    xpos, ypos = (1, 1)
    q = []
    q.append((xpos, ypos, d))
    room[xpos][ypos] += 1
    tail = [[1, 1]]
    while q:
        xpos, ypos, d = q.pop(0)
        x = xpos + dx[d]
        y = ypos + dy[d]

        #show(room)

        time += 1
        if 1 <= x < len(room) and 1 <= y < len(room):
            # print(x, y)
            room[x][y] += 1

            if room[x][y] > 1:
                break

            if [x, y] not in apple_position:
                if tail:
                    t = tail.pop(0)
                room[t[0]][t[1]] -= 1
                tail.append([x, y])
                #print(tail)
            else:
                tail.append([x, y])
                apple_position.remove([x, y])

            for di in direct:
                if time == int(di[0]):
                    d = (d + 1)%4 if di[1] == 'D' else (d - 1)%4

            q.append((x, y, d))

    return time

def show(room):
    for i in range(1, len(room)):
        for j in range(1, len(room)):
            print(room[i][j], end=' ')
        print()
    print()

n = int(input())
k = int(input())

apple_position = [list(map(int, input().split())) for _ in range(k)]
#print(apple_position)

l = int(input())
direct = [list(input().split()) for _ in range(l)]
#print(direct)

room = [[0] * (n + 1) for _ in range(n + 1)]

print(simulation(room, apple_position, direct))