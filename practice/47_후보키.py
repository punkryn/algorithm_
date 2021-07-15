# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations

def solution(relation):
    answer = 0

    column = list(range(len(relation[0])))
    n = len(column)
    dele = []
    for i in range(1, n + 1):
        for key in combinations(column, i):
            _dict = dict()
            flag = False

            for tuple in relation:
                tmp = set()
                for k in key:
                    tmp.add(tuple[k])

                tmp = sorted(list(tmp))
                #print(tmp)
                tmp = ''.join(list(tmp))

                if tmp in _dict.keys():
                    flag = True
                    # _dict[tmp] += 1
                else:
                    _dict[tmp] = 0

            if not flag:
                if mini(dele, list(key)):
                    dele.append(list(key))
                    answer += 1

    return answer

def mini(dele, key):
    # print(dele, key)
    for i in range(1, len(key) + 1):
        for comb in list(combinations(key, i)):
            comb = list(comb)
            if comb in dele or comb[::-1] in dele:
                return False
    return True


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))