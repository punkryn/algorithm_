# https://programmers.co.kr/learn/courses/30/lessons/81302#fn1

from itertools import combinations

def solution(places):
    answer = []

    for place in places:
        room = []
        for i, waiting in enumerate(place):
            room.append([w for w in waiting])

        p = []
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    p.append([i, j])

        breach = []
        for comb in combinations(p, 2):
            first = comb[0]
            second = comb[1]

            x1, y1 = first
            x2, y2 = second

            distance = abs(x2 - x1) + abs(y2 - y1)
            if distance == 1:
                breach.append(list(comb))
            elif distance == 2:
                #print(x1, x2, y1, y2)
                if x1 == x2:
                    if room[x1][min(y1, y2) + 1] != 'X':
                        breach.append(list(comb))
                elif y1 == y2:
                    if room[min(x2, x1) + 1][y1] != 'X':
                        breach.append(list(comb))
                else:
                    if x1 - x2 == y1 - y2:
                        if room[min(x1, x2) + 1][min(y1, y2)] != 'X' or room[min(x1, x2)][min(y1, y2) + 1] != 'X':
                            breach.append(list(comb))
                    else:
                        if room[min(x1, x2) + 1][max(y1, y2)] != 'X' or room[min(x1, x2)][min(y1, y2)] != 'X':
                            breach.append(list(comb))

        #print(breach)
        if breach:
            answer.append(0)
        else:
            answer.append(1)

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))