def mergesort(a):
    k = len(a) // 2
    if len(a) > 1:
        return merge(mergesort(a[:k]), mergesort(a[k:]))
    else:
        return a

def merge(p, q):
    c = []
    while p and q:
        p1 = p.pop(0)
        q1 = q.pop(0)

        if p1 < q1:
            c.append(p1)
            q.insert(0, q1)
        elif p1 > q1:
            c.append(q1)
            p.insert(0, p1)
        else:
            c.append(p1)
            c.append(q1)

    return c + p + q


arr = [9, 1,8, 2,7,3,6,4,5]
arr = mergesort(arr)
print(arr)