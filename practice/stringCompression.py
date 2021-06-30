# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = s
    for length in range(1, len(s) // 2 + 1):
        results = (comp(s, length))
        string = ''
        # print(results)
        for result in results:
            tmp = (result[1] - result[0] + 1) // length
            if tmp == 1:
                string += s[result[0]: result[0] + length]
            else:
                string += str(tmp) + s[result[0]: result[0] + length]

        if results[-1][1] < len(s) - 1:
            string += s[results[-1][1] + 1:]

        # print(answer, string)
        if len(answer) > len(string):
            answer = string

    return len(answer)

def comp(s, l):
    result = []
    start = 0
    end = l - 1
    pre = s[:l]
    for i in range(l, len(s), l):
        if i + l > len(s):
            now = s[i:]
        else:
            now = s[i: i + l]

        # print(pre, now, start, end, i)
        if pre == now:
            end += l
            if i + l >= len(s):
                result.append((start, end))
        else:
            result.append((start, end))
            start = end + 1
            end = start + l - 1

        pre = now

    return result

s = "abcabcdede"
print(solution(s))