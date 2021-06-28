# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

def solution(name):
    answer = 0

    tmp = 0
    aList = []
    for i in range(len(name)):
        aList.append('A')
    for i in range(len(name)):
        tmp += (ord(name[i]) - ord('A') if ord(name[i]) < ord('N') else 91 - ord(name[i]))

        aList[i] = name[i]

        if ''.join(aList) == name:
            break

        if i == len(name) - 2 and name[i + 1] == 'A':
            break
        else:
            tmp += 1

    tmp2 = 0
    index = 0

    aList = []
    for i in range(len(name)):
        aList.append('A')

    while True:
        tmp2 += (ord(name[index]) - ord('A') if ord(name[index]) < ord('N') else 91 - ord(name[index]))

        aList[index] = name[index]

        if (index % len(name)) == 2 and name[index - 1] == 'A':
            break
        else:
            index -= 1
            tmp2 += 1

        if ''.join(aList) == name:
            tmp2 -= 1
            break

    print('tmp2', tmp2)

    index = 0
    aList = []
    for i in range(len(name)):
        aList.append('A')
    iList = chain(name)
    tmp3 = int(1e9)
    if iList != []:
        tmp3 = 0
        start, count = max(iList, key=lambda x: x[1])
        if (start - 1) * 2 < count:
            for i in range(start):
                tmp3 += (ord(name[i]) - ord('A') if ord(name[i]) < ord('N') else 91 - ord(name[i]))
            tmp3 += ((start - 1) * 2)
            count2 = 0
            for i in range(len(name) - 1, start + count - 1, -1):
                tmp3 += (ord(name[i]) - ord('A') if ord(name[i]) < ord('N') else 91 - ord(name[i]))
                count2 += 1
            tmp3 += count2

    answer = min(tmp, tmp2, tmp3)

    tmpName = ''
    for i in range(len(name)):
        tmpName += 'A'

    if tmpName == name:
        answer = 0

    return answer

def chain(name):
    tmp = 0
    iList = []
    start = 0
    for i in range(len(name)):
        if name[i] == 'A':
            if start == 0:
                start = i
            tmp += 1
        else:
            if tmp > 1:
                iList.append((start, tmp))
            tmp = 0
            start = 0
    return iList

alphabet = []
for i in range(65, 91):
    alphabet.append(chr(i))

name = 'JAN'
print(alphabet)
for a in name:
    print(ord(a), end=' ')
print()
for a in name:
    print(ord(a) - ord('A'), end=' ')
print()
print(solution(name))