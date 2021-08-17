# https://programmers.co.kr/learn/courses/30/lessons/60060

def bsleft(start, end, word):
    target = '?'
    result = 0
    while start <= end:
        mid = (start + end) // 2
        # print(start, end, mid, word[mid])
        if word[0] == '?':
            if word[mid] == target:
                start = mid + 1
            else:
                end = mid - 1
            result = end
        elif word[-1] == '?':
            if word[mid] == target:
                end = mid - 1
            else:
                start = mid + 1
            result = start
    return result

def wordbs(start, end, target, words):
    left, right = -1, -1
    tmp1 = start
    tmp2 = end
    while start <= end:
        mid = (start + end) // 2
        if len(words[mid]) >= target:
            end = mid - 1
        else:
            start = start + 1
        left = end + 1

    start = tmp1
    end = tmp2
    while start <= end:
        mid = (start + end) // 2
        if len(words[mid]) > target:
            end = mid - 1
        else:
            start = start + 1
        right = start

    return left, right

def wordbs2(start, end, target, words):
    left, right = -1, -1
    tmp1 = start
    tmp2 = end
    while start <= end:
        mid = (start + end) // 2
        #print(words[mid][0], target, words[mid][0] >= target)
        if (words[mid][0]) >= target:
            end = mid - 1
        else:
            start = mid + 1
        left = end + 1

    start = tmp1
    end = tmp2
    while start <= end:
        mid = (start + end) // 2
        #print(start, end, mid)
        if (words[mid][0]) > target:
            end = mid - 1
        else:
            start = mid + 1
        right = start - 1

    return left, right

def solution(words, queries):
    answer = []

    words.sort()

    rwords = []
    for word in words:
        rwords.append(''.join((reversed(word))))
    rwords.sort()

    for query in queries:
        wildcard = bsleft(0, len(query) - 1, query)
        #wildrange = query[:wildcard + 1] if query[0] == '?' else query[wildcard:]
        #wildrange = (0, wildcard) if query[0] == '?' else (wildcard, len(query) - 1)
        wordrange = (0, wildcard - 1) if query[0] != '?' else (wildcard + 1, len(query) - 1)
        start, end = wordrange
        count = 0
        # left, right = wordbs(0, len(words) - 1, len(query), words)
        #print(left, right)

        if query[0] == '?':
            left, right = wordbs2(0, len(rwords) - 1, query[-1], rwords)
            query = ''.join(reversed(query))
            for word in rwords[left: right + 1]:
                #print(word[len(word) - end - 1: len(word) - start], query[len(word) - end - 1: len(word) - start])
                if len(word) == len(query) and word[len(word) - end - 1: len(word) - start] == query[len(word) - end - 1: len(word) - start]:
                    count += 1
        else:
            left, right = wordbs2(0, len(words) - 1, query[0], words)
            for word in words[left: right + 1]:
                if len(word) == len(query) and word[start: end + 1] == query[start: end + 1]:
                    count += 1

        #print(rwords)
        #print(left, right)



        answer.append(count)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))