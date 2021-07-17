# https://programmers.co.kr/learn/courses/30/lessons/42892

class Node:
    def __init__(self, left, right, num):
        self.number = num
        self.left = left
        self.right = right

    def print(self):
        print(self.number)

def preorder(nodeinfo):
    n = []
    for noe in nodeinfo:
        n.append(Node(None, None, noe[0]))

    tree = []

    i = 1
    for node in n:
        if nodeinfo[i][2] == nodeinfo[i + 1][2]:
            node.left = n[i]
            node.right = n[i + 1]
            i += 2
        else:
            pass


def solution(nodeinfo):
    answer = [[]]

    nodeinfo_ = []
    level = max(nodeinfo, key=lambda x: x[1])[1]
    for i, node in enumerate(nodeinfo, start=1):
        node[1] = level - node[1]
        nodeinfo_.append([i] + node)

    nodeinfo = nodeinfo_
    nodeinfo.sort(key=lambda x: (x[2], x[1]))

    print(nodeinfo)


    return answer

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))