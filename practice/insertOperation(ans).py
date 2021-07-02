n = int(input())

fomula = list(map(int, input().split()))

add, sub, mul, div = (map(int, input().split()))

min_value = 1e9
max_value = -1e9

def dfs(count, result):
    global add, sub, mul, div, min_value, max_value

    if count == n:
        min_value = min(min_value, result)
        max_value = max(max_value, result)
    else:
        if add > 0:
            add -= 1
            dfs(count + 1, result + fomula[count])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(count + 1, result - fomula[count])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(count + 1, result * fomula[count])
            mul += 1
        if div > 0:
            div -= 1
            if result < 0:
                result *= (-1)
                result //= fomula[count]
                result *= (-1)
                dfs(count + 1, result)
            else:
                dfs(count + 1, result // fomula[count])
            div += 1

dfs(1, fomula[0])

print(max_value)
print(min_value)