# 2
# 5 6
# 0 0 1 0

# https://www.acmicpc.net/problem/14888

def dfs(pos, end, result):
    print(pos, end, result, value, op, sequence)
    if pos == end:
        value[0] = max(value[0], result)
        value[1] = min(value[1], result)
        return value
    else:
        # pos = start
        #print(pos)
        for i in range(4):
            #print('i', i)
            if op[i] > 0:
                op[i] -= 1
                #print(i)
                tmp = result
                if i == 0:
                    result += sequence[pos + 1]
                elif i == 1:
                    result -= sequence[pos + 1]
                elif i == 2:
                    result *= sequence[pos + 1]
                elif i == 3:
                    result = result // sequence[pos + 1] if result >= 0 else -((-result) // sequence[pos + 1])
                #print('i, result', i, result, sequence[pos], sequence[pos + 1])

                dfs(pos + 1, end, result)
                op[i] += 1
                result = tmp


n = int(input())

sequence = list(map(int, input().split()))

op = list(map(int, input().split()))

result = 0
maxvalue = 0
minvalue = int(1e9)
value = [maxvalue, minvalue]
dfs(0, n - 1, sequence[0])

print(value[0])
print(value[1])