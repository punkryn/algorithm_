def solution(word):
    global count
    global answer
    bt([], word, 0)

    return answer

def bt(arr, word, depth):
    global count
    global answer
    if depth == 5:
        return
    else:
        for w in ['A', 'E', 'I', 'O', 'U']:
            arr.append(w)
            print(arr)
            count += 1
            if ''.join(arr) == word:
                answer = count

            bt(arr, word, depth + 1)

            arr.pop()

word = 'EIO'
count = 0
answer = 0
print(solution(word))