# https://programmers.co.kr/learn/courses/30/lessons/81303

from bisect import bisect_left
def solution(n, k, cmd):
    N = n

    data = [i for i in range(n)]

    # 삭제된 인덱스들을 넣어놓을 스택
    rm_stack = []

    for order in cmd:
        #print(k, data)

        # C나 Z
        if len(order) == 1:
            #삭제
            if order == 'C':
                num = data.pop(k)
                rm_stack.append(num) # 인덱스와 값을 저장
                if k == len(data):
                    k -= 1
            # 복원
            else:
                q = rm_stack.pop()
                idx = bisect_left(data, q)
                if q < data[k]:
                    k += 1
                data.insert(idx,q)

        else:
            do, num = order.split()
            num = int(num)
            # 아래로이동 -> K를 증가
            if do == 'D':
                k += num

            # 위로이동 -> K를 감소
            else:
                k -= num

    #print(k, data)

    answer = ['O'] * N
    for i in rm_stack:
        answer[i] = 'X'

    #print(answer)
    return ''.join(answer)

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
#cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))