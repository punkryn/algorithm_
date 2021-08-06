# 10806

import heapq

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    A = list(map(int, input().split()))
    k = int(input())

    q = []
    q.append((0, k))
    while q[0][1] > 0:
        now = heapq.heappop(q)

        heapq.heappush(q, (now[0] + now[1], 0))
        for i in range(n):
            print(q)
            heapq.heappush(q, (now[0] + now[1] % A[i], now[1] // A[i]))

    print("#{} {}".format(test_case, q[0][0]))