# https://www.acmicpc.net/problem/18406

# 123402

n = input()

length = len(n)
left = (n[0: length // 2])
right = (n[length // 2:])

lvalue = 0
for word in left:
    lvalue += int(word)

rvalue = 0
for word in right:
    rvalue += int(word)

if lvalue == rvalue:
    print("LUCKY")
else:
    print("READY")