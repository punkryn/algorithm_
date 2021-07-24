# ({)}

T = int(input())

for test_case in range(1, T + 1):
    raw = input()
    stack = []
    flag = False
    for r in list(raw):
        if r == '(' or r == '{':
            stack.append(r)
        elif r == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = True
                break
        elif r == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                flag = True
                break
    if stack or flag:
        print(f'#{test_case}', 0)
    else:
        print(f'#{test_case}', 1)