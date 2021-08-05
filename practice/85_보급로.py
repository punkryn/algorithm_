import heapq

def go(x, y, total):
    # print(x, y)
    global minvalue
    if (x == n - 1 and y == n - 1) or minvalue < total:
        #print(total)
        minvalue = min(minvalue, total)
        heapq.heappush(result, total)
        return

    candidate = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= ny < n and 0 <= nx < n:
            if visited[nx][ny] == 0:
                candidate.append([map_[nx][ny], nx, ny])
    # print(candidate)
    a = min(candidate)[0]
    for cand in candidate:
        time, nx, ny = cand
        if time == a:
            visited[nx][ny] = 1
            go(nx, ny, total + time)
            visited[nx][ny] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

T = int(input())

for test_case in range(1, T + 1):
    minvalue = int(1e9)
    n = int(input())
    map_ = [list(map(int, input().strip())) for _ in range(n)]
    result = []
    visited = [[0] * n for _ in range(n)]
    go(0, 0, 0)
    # print(result)
    print(heapq.heappop(result))