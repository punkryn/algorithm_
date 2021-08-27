from itertools import permutations

def go(depth, length, dices, result, string, visited):
    if depth == length:
        ans = int(string)
        # print(ans, length)
        result.add(ans)
        return

    for i in range(length):
        if visited[i] == 1:
            continue
        for j in range(6):
            if i == 0 and dices[i][j] == 0:
                # print("123", i, j)
                continue
            visited[i] = 1
            go(depth + 1, length, dices, result, string + str(dices[i][j]), visited)
            visited[i] = 0

def solution(dice):
    answer = 0

    length = len(dice)
    result = set()

    for i in range(1, length + 1):
        for comb in list(permutations(dice, i)):
            visited = [0] * i
            # print(comb)
            go(0, i, comb, result, '', visited)

    start = 1
    while True:
        if start in result:
            start += 1
            continue
        else:
            break

    answer = start

    return answer

dice = [[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]
print(solution(dice))

'''
문제 설명
0 ~ 9 사이의 숫자가 쓰여있는 정육면체 주사위 n개가 주어졌을 때, 당신은 이 주사위로 만들 수 없는 가장 작은 자연수를 찾으려 합니다. 주사위로 숫자를 만드는 방법은 다음과 같습니다.

주사위를 모두 굴립니다.
그중 1 ~ n개를 임의로 선택합니다.
선택한 주사위를 임의의 순서로 왼쪽부터 오른쪽까지 나열합니다. 단, 0이 나온 주사위를 맨 왼쪽에 놓을 수 없습니다. 0이 나온 주사위 하나만 선택하는 것도 불가능합니다.
임의로 나열한 주사위를 왼쪽부터 읽어 숫자를 만듭니다. 예를 들어, 2개의 주사위가 선택되었고 왼쪽 주사위는 1, 오른쪽 주사위는 2가 나왔다면 숫자 12를 만듭니다.
주사위는 원하는 숫자가 나올 때까지 계속 굴릴 수 있습니다.

예를 들어, 주사위 두 개가 주어지고, 각 주사위에 쓰여있는 숫자가 [1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]라고 할 때 만들 수 있는 숫자는 다음과 같습니다.

1, 2, 3, ..., 20, 21, 27, 28, ...

따라서 만들 수 없는 가장 작은 자연수는 22입니다.

주사위의 정보를 담은 2차원 정수 배열 dice가 매개변수로 주어질 때, 만들 수 없는 가장 작은 자연수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ dice의 길이 = 주사위의 개수 ≤ 4
dice의 원소는 각 주사위에 쓰인 수를 담고 있는 길이 6인 정수 배열입니다.
주사위는 항상 0 이상 9 이하인 수가 6개 쓰여있으며, 중복된 수가 쓰여있을 수도 있습니다.
입출력 예
dice	result
[[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]	22
[[0, 1, 5, 3, 9, 2], [2, 1, 0, 4, 8, 7], [6, 3, 4, 7, 6, 5]]	66
입출력 예 설명
입출력 예 #1

문제 예시와 동일합니다.

입출력 예 #2

주사위를 굴려 1 ~ 65까지 모두 만들 수 있습니다. 하지만 어떠한 방법으로도 66을 만들 수는 없습니다. 따라서 정답은 66입니다.
'''