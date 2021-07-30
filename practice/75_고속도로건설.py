def find_parent(parent, r):
    if parent[r] != r:
        parent[r] = find_parent(parent, parent[r])
    return parent[r]

def union(parent, r1, r2):
    r1 = find_parent(parent, r1)
    r2 = find_parent(parent, r2)

    if r1 < r2:
        parent[r2] = r1
    else:
        parent[r1] = r2

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    M = int(input())
    roads = []
    for _ in range(M):
        s, e, c = map(int, input().split())
        roads.append([c, s, e])

    parent = [i for i in range(N + 1)]
    roads.sort()
    total = 0

    for road in roads:
        cost, s, e = road
        if find_parent(parent, s) != find_parent(parent, e):
            total += cost
            union(parent, s, e)

    print("#" + str(test_case), total)