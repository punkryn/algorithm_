import bisect

T = int(input())

def upper_bound(i, j, target):
    ans = j
    while i <= j:
        mid = (i + j) // 2
        if len(names[mid]) > target:
            ans = mid - 1
            j = mid - 1
        else:
            i = mid + 1
    return ans

for test_case in range(1, T + 1):
    n = int(input())
    names = [input().strip() for _ in range(n)]
    # print(names)

    names.sort(key=lambda x: (len(x), x))
    # print(names)
    print("#" + str(test_case))
    idx = 0
    while idx < n:
        name = names[idx]
        # left = bisect.bisect_left(names, name)
        # right = bisect.bisect_right(names, name)
        right = upper_bound(idx, n-1, len(name))
        right2 = bisect.bisect_right(names[idx:right+1], name)
        right2 -= 1
        right2 += idx

        #print('right', right, right2, idx)

        if idx == right2:
            print(name)
            idx += 1
        else:
            print(name)
            idx += (right2 - idx + 1)