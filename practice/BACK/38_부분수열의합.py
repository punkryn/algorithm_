# 5 0
# -7 -3 -2 5 8

# https://www.acmicpc.net/problem/1182

from sys import stdin
import copy

n, s = map(int, input().split())
seq = list(map(int, stdin.readline().split()))

count = 0
def bt(s, seq, n, depth, arr):
    global count
    #print(arr)
    if n == depth:
        return
    else:
        seq_tmp = copy.deepcopy(seq)
        while seq_tmp:
            i = seq_tmp.pop()
            arr.append(i)
            if sum(arr) == s:
                count += 1

            bt(s, seq_tmp, n, depth+1, arr)

            arr.pop()


arr = []
bt(s, seq, n, 0, arr)
#print(arr)
print(count)