def search(answer, p):
    start = 1
    end = 1
    cnt = 0

    while end < 1e6 + 1:
        print(end, start, p, cnt, answer)
        if end == 23:
            break
        if visited[end]:
            cnt += 1
            end += 1
            answer = max(answer, cnt)
        else:
            if p == 0:
                answer = max(answer, cnt)
                if not visited[start]:
                    p += 1
                start += 1
                cnt -= 1
            else:
                p -= 1
                cnt += 1
                end += 1
    return answer

T = int(input())

# 3 4 5 6 7 10 11

# 1
# 13 8
# 1 3 6 7 8 9 11 15 16 17 18 19 20
for test_case in range(1, T + 1):
    n, p = map(int, input().split())
    studyday = list(map(int, input().split()))

    visited = [0] * int(1e6 + 1)

    for day in studyday:
        visited[day] = 1

    answer = p + 1

    answer = search(answer, p)

    #print(day)
    print("#" + str(test_case), answer)