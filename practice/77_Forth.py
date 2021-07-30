T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _list = list(input().split())
    stack = []
    symbol = ['/', '+', '*', '-']
    flag = True
    for l in _list:

        if l not in symbol:
            stack.append(l)
        elif l in symbol:

            try:
                t = int(stack.pop())
                f = int(stack.pop())
                if l == symbol[0]:
                    result = f // t
                elif l == symbol[1]:
                    result = f + t
                elif l == symbol[2]:
                    result = f * t
                elif l == symbol[3]:
                    result = f - t

                stack.append(result)
            except:
                print(f'#{test_case}', 'error')
                flag = False
                break

        elif l == '.':
            print(f'#{test_case}', stack[0])
            break
    if stack and stack[-1] == '.' and len(stack) <= 2:
        print(f'#{test_case}', stack[0])
    else:
        if flag:
            print(f'#{test_case}', 'error')