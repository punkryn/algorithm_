# https://programmers.co.kr/learn/courses/30/lessons/60058

def solution(p):
    answer = ''
    if p == '':
        return p

    if check(p):
        return p

    pivot = cut(p)
    u = p[:pivot]
    v = p[pivot:]

    if check(u):
        return u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'

        answer += ucut(u)

    return answer

def cut(p):
    left = 0
    right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        elif p[i] == ')':
            right += 1

        if left == right:
            break

    return left + right

def check(p):
    stack = []
    for i in range(len(p)):
        if p[i] == '(':
            stack.append('(')
        elif p[i] == ')':
            if stack:
                stack.pop()
            else:
                return False

    if not stack:
        return True
    else:
        return False

def ucut(u):
    u = u[1:-1]
    tmp = []
    for i in range(len(u)):
        if u[i] == '(':
            tmp.append(')')
        elif u[i] == ')':
            tmp.append('(')
    return ''.join(tmp)

p = "))(()("
print(solution(p))