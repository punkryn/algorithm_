# https://acmicpc.net/problem/1439

# 0001100

# 연속한 숫자들의 그룹을 생성한다.
# chain이 반환하는 리스트는 [시작인덱스, 연속한 숫자들의 마지막 인덱스]로 구성
# 사실 그룹의 개수만 세면 되기 때문에 그룹의 구성은 상관없다.
# 그룹의 개수가 홀수든 짝수든 2로 나눈 정수의 몫만 취하면 된다.
# 0과 1로만 이루어져 있기 때문에 그룹은 항상 0그룹 1그룹 번갈아 나온다.

def chain(s):
    index = 0
    start = 0
    result = []
    while index < len(s):
        next = index + 1
        if next == len(s):
            result.append([start, index])
            break

        if s[index] == s[next]:
            index += 1
        else:
            result.append([start, index])
            start = next
            index += 1
    return result

s = input()

group = chain(s)
#group = sorted(group, key=lambda x: x[1] - x[0], reverse=True)
print(len(group) // 2)