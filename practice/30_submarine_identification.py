# 10010111

# 1001011
# 10011001

# https://www.acmicpc.net/problem/2671

n = input()

index = 0
condition = True
f = False
f2 = False
f3 = False
s = False
answer = 'SUBMARINE'
while index < len(n):
    #print(index, n[:index + 1])
    if len(n) == 2:
        if n[:2] == '01':
            answer = 'SUBMARINE'
            break
    elif len(n) == 3:
        answer = 'NOISE'
        break
    elif n[-1] == '0':
        answer = 'NOISE'
        break
    else:
        if not f and not f2:
            #print('a')
            if f3:
                if n[index] == '1':
                    index += 1
                    f2 = True
                    continue

                f3 = False

                if len(n) >= index + 2 and n[index: index + 2] == '01':
                    index += 2
                    continue

                index -= 1

                if len(n) >= index + 3 and n[index: index + 3] == '100':
                    index += 3
                    f = True
                    continue
            else:
                if len(n) >= index + 2 and n[index: index + 2] == '01':
                    index += 2
                    continue

                if len(n) >= index + 3 and n[index: index + 3] == '100':
                    index += 3
                    f = True
                    continue

                answer = 'NOISE'
                break
        elif f:
            #print('b')
            if n[index] == '0':
                index += 1
                continue
            else:
                index += 1
                f = False
                f2 = True
                continue
        elif f2:
            #print('c')
            if n[index] == '1':
                index += 1
                f2 = False
                f3 = True
                continue
            else:
                f2 = False
                continue

#print(index)
print(answer)

# import re
#
# n = input()
#
# p = re.compile('(100+1+|01)+')
# m = p.fullmatch(n)
# if m:
#     print('SUBMARINE')
# else:
#     print('NOISE')