# 1
# 5
# 3 5
# 5 8
# 6 18
# 2 10
# 9 20

import heapq

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    S = [0]
    F = [0]
    for _ in range(N):
        s, f = map(int, input().split())
        S.append(s)
        F.append(f)

    F.sort()
    solvedSum = [0] * (N + 1)
    solved = []
    for i in range(1, N + 1):
        if solvedSum[i-1] + S[i] <= F[i]:
            solvedSum[i] = solvedSum[i - 1] + S[i]
            #solved.append(S[i])
            heapq.heappush(solved, (-S[i], S[i]))
        else:
            if solved:
                # heapq._heapify_max(solved)
                j = heapq.heappop(solved)[1]
                #print(j, solved, i)
                if j > S[i]:
                    #print(solved)
                    #print(j, S[i])
                    solvedSum[i] = solvedSum[i - 1] - j + S[i]
                    heapq.heappush(solved, (-S[i], S[i]))

                else:
                    heapq.heappush(solved, (-j, j))
        #print(solvedSum)
    #print(solved)
    print("#" + str(test_case), len(solved))