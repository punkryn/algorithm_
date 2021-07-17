# https://programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    answer = 0

    i = 0
    n = len(s)
    ans = []
    string = []

    num = {'zero': 0, 'one': 1,'two': 2,'three': 3,'four':4 ,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine':9}

    for key in num.keys():
        s = s.replace(key, str(num[key]))

    answer = s

    # while i < n:
    #     if ''.join(string) in num:
    #         ans.append(''.join(string))
    #         string = []
    #
    #     if s[i].isdigit():
    #         ans.append(s[i])
    #         string = []
    #     else:
    #         string.append((s[i]))
    #
    #     #print(string)
    #
    #     i += 1
    #
    # if string:
    #     if ''.join(string) in num:
    #         ans.append(''.join(string))
    # #print(ans)
    # answer = ''
    # for i, a in enumerate(ans):
    #     #print(a)
    #
    #     if a.isdigit():
    #         answer += a
    #     else:
    #         answer += str(num[a])

    #print(answer)

    return int(answer)

s = 'one4seveneight'
print(solution(s))