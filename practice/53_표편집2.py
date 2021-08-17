# https://programmers.co.kr/learn/courses/30/lessons/81303

from collections import deque

class link:
    def __init__(self, idx):
        self.next = None
        self.idx = idx

    def connect(self, nxt):
        self.next = nxt

def solution(n, k, cmd):
    answer = ''

    linked = [link(i) for i in range(n)]
    for i in range(n - 1):
        linked[i].next = linked[i + 1]

    linked = linked[0]
    cmd = deque(cmd)
    delete = []
    while cmd:
        command = cmd.popleft()
        com = command.split()

        # print(com)
        if len(com) > 1:
            if com[0] == 'D':
                k += int(com[1])
            elif com[0] == 'U':
                k -= int(com[1])
        elif len(com) == 1:
            if com[0] == 'C':
                tmp = linked
                if k == 0:
                    tmp.next = None
                    delete.append(tmp)
                    linked = linked.next
                elif k > 0:
                    for j in range(1, k):
                        tmp = tmp.next

                    if tmp.next.next == None:
                        delete.append(tmp.next)
                        tmp.next = None
                    else:
                        delete.append(tmp.next)
                        tmp.next = tmp.next.next

                # delete.append(table.pop(k))
                # if k == len(table):
                #     k -= 1
            elif com[0] == 'Z':
                recover = delete.pop()
                if recover.idx > k:
                    for j in range
                elif recover[0] < k:
                    table.insert(recover[0], recover)
                    k += 1

    return answer

n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
#cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]
print(solution(n, k, cmd))