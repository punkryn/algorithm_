def solution(letters, k):
    answer = ''

    stack = [letters[0]]
    k = len(letters) - k
    for letter in letters[1:]:
        while stack and k > 0 and stack[-1] < letter:
            stack.pop()
            k -= 1

        stack.append(letter)

    if k != 0:
        stack = stack[:-k]

    answer = answer.join(stack)

    return answer

letters = 'bgajzab'
k = 3
print(solution(letters, k))