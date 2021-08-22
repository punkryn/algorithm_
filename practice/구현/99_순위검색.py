# https://programmers.co.kr/learn/courses/30/lessons/72412

from bisect import bisect_left

def lower_bound(left, right, arr, target):
    while left < right:
        mid = (left + right)//2

        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

def go(depth, qs, ele, cands, score):
    global total
    if depth == 4:
        # print(ele)

        if ele in cands.keys():
            # print(cands[ele])
            total += len(cands[ele]) - lower_bound(0, len(cands[ele]), cands[ele], score)
            # total += len(cands[ele]) - bisect_left(cands[ele], score)
        return

    # print(qs)
    for i in range(depth, 4):
        # print(qs)
        e = qs[i]
        if e == '-':
            # print(infos[i], i, ele, qs, depth)
            if depth == i:
                for cand in infos[i]:
                    go(depth + 1, qs, ele + cand, cands, score)
        else:
            go(depth + 1, qs, ele + e, cands, score)


def solution(info, query):
    global total
    answer = []

    cand = {}
    for inf in info:
        tmp = inf.split()
        keys = ''.join(tmp[:-1])
        if keys not in cand.keys():
            cand[keys] = [int(tmp[-1])]
        else:
            cand[keys].append(int(tmp[-1]))

    for key in cand.keys():
        cand[key].sort()

    for q in query:
        qs = q.split()
        score = int(qs[7])
        qs = [qs[0]] + [qs[2]] + [qs[4]] + [qs[6]]
        total = 0
        go(0, qs, '', cand, score)
        answer.append(total)

    print(answer)
    return answer

infos = [['java', 'python', 'cpp'],
['backend', 'frontend'],
['junior', 'senior'],
['pizza', 'chicken']]
total = 0

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
# query = ["- and - and - and - 150"]
solution(info, query)