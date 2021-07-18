# https://www.acmicpc.net/contest/problem/658/1
# https://www.acmicpc.net/contest/view/658
def sortby(x):
    return x[0]

n, m = map(int, input().split())

filename = [list(input().split('.')) for _ in range(n)]
ext = [input() for _ in range(m)]

filename.sort(key=lambda x: x[0])
print(filename)
