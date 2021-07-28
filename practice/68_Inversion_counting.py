# 1
# 5
# 4 1 3 2 5

def mergesort(A, left, right):
    global total
    if left < right:
        mid = (left + right) // 2
        mergesort(A, left, mid)
        mergesort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    global total

    p = left
    q = mid + 1
    idx = left

    while p <= mid and q <= right:
        if A[p] > A[q]:
            C[idx] = A[q]
            total += mid - p + 1
            idx += 1
            q += 1
        else:
            C[idx] = A[p]
            p+=1
            idx += 1

    while p <= mid:
        C[idx] = A[p]
        idx+=1
        p+=1

    while q <= right:
        C[idx] = A[q]
        idx+=1
        q+=1

    for i in range(left, right+1):
        A[i] = C[i]


#import sys

#sys.stdin = open()

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    A = list(map(int, input().split()))
    C = [0] * n
    total = 0
    mergesort(A, 0, n - 1)
    #print(A)

    print("#" + str(test_case), total)