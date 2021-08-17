import heapq

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    distance[0][0] = 0
    while q:
        dist, x, y = heapq.heappop(q)

        if distance[x][y] < dist:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                cost = dist + map_[nx][ny]
                if cost < distance[nx][ny]:
                    distance[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    map_ = [list(map(int, input().strip())) for _ in range(n)]
    distance = [[int(1e9)] * n for _ in range(n)]
    dijkstra()
    print("#{} {}".format(test_case, distance[n-1][n-1]))