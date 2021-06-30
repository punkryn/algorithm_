def solution(s):
    answer = 0

    length = len(s)

    if length <= 1:
        return length

    result = []

    for i in range(1, length // 2 + 1):
        tmp = ''
        count = 1
        sw = 0
        for j in range(0, length - i, i):
            # print(s[j:j + i], s[j + i:j + i + i])
            # print(j, i)
            # print(s[j:j + i], s[j + i:j + i + i])
            if s[j:j + i] == s[j + i:j + i + i]:
                count += 1
            else:
                tmp += ((str)(count if count != 1 else '') + s[j: j + i])
                count = 1
                # print(tmp)

        tmp += str(count if count != 1 else '') + s[j + i:]
        # print(tmp)
        result.append(len(tmp)) if len(tmp) > 0 else 1
    # print(result)
    answer = min(result)
    return answer