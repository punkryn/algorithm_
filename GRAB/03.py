def go(depth, wordset, cards, matrix):
    global total
    if depth == len(cards):
        flag = True
        # print(wordset)
        for key in wordset.keys():
            if wordset[key] > 0:
                flag = False
        if flag:
            total += 1
            # print(matrix)
        return

    for i in range(len(cards)):
        # print(i)
        w = cards[depth][i]
        if w in wordset.keys() and wordset[w] > 0:
            matrix[depth] = i
            # print(matrix)
            flag2 = False
            for j in range(depth):
                if matrix[j] == matrix[depth]:
                    matrix[depth] = -1
                    flag2 = True
                    break
            if flag2:
                continue

            wordset[w] -= 1
            go(depth + 1, wordset, cards, matrix)
            wordset[w] += 1
            matrix[depth] = -1

    go(depth + 1, wordset, cards, matrix)



def solution(word, cards):
    global total
    answer = -1

    wordset = {}
    for w in word:
        if w not in wordset.keys():
            wordset[w] = 1
        else:
            wordset[w] += 1

    matrix = [-1] * len(cards)

    go(0, wordset, cards, matrix)
    # print(total)

    return total

total = 0

word = "BAB"
cards = ["ZZBZ", "BAZB","XBXB","XBAX"]

print(solution(word, cards))