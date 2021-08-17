# https://programmers.co.kr/learn/courses/30/lessons/81303

from collections import deque

def solution(n, k, cmd):
    answer = ''

    table = [[i] for i in range(n)]
    delete = []
    cmd = deque(cmd)
    while cmd:
        command = cmd.popleft()

        com = command.split()

        #print(com)
        if len(com) > 1:
            if com[0] == 'D':
                k += int(com[1])
            elif com[0] == 'U':
                k -= int(com[1])
        else:
            if com[0] == 'C':
                delete.append(table.pop(k))
                if k == len(table):
                    k -= 1
            elif com[0] == 'Z':
                recover = delete.pop()
                if recover[0] > k:
                    table.insert(recover[0], recover)
                elif recover[0] <= k:
                    table.insert(recover[0], recover)
                    k += 1


        #print(table, delete, k)
    #print(table, delete)

    result = ['O'] * n
    for idx in table:
        result[idx[0]] = 'O'

    for idx in delete:
        result[idx[0]] = 'X'

    answer = ''.join(result)

    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
#cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))