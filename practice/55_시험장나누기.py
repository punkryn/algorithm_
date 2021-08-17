# https://programmers.co.kr/learn/courses/30/lessons/81305

def solution(k, num, links):
    answer = 0

    root = 0
    room = list(range(len(num)))
    for l, r in links:
        if l != -1:
            if l in room:
                room.remove(l)
        if r != -1:
            if r in room:
                room.remove(r)

    root = room[0]



    return answer

k = 3
num =[12, 30, 1, 8, 8, 6, 20, 7, 5, 10, 4, 1]
links = [[-1, -1], [-1, -1], [-1, -1], [-1, -1], [8, 5], [2, 10], [3, 0], [6, 1], [11, -1], [7, 4], [-1, -1], [-1, -1]]
print(solution(k, num, links))