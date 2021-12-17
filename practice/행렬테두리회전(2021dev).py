# https://programmers.co.kr/learn/courses/30/lessons/77485?language=python3
def solution(rows, columns, queries):
    answer = []

    matrix = [[-1] * (columns + 2) for _ in range(rows + 2)]
    cnt = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = cnt
            cnt += 1
    # print(matrix)

    def rotate(query):
        matrix_sub = [[-1] * (columns + 2) for _ in range(rows + 2)]
        leftup = (query[0], query[1])
        rightdown = (query[2], query[3])
        # print(leftup, rightdown)
        minValue = int(1e9)
        for i in range(leftup[1], rightdown[1] + 1):
            matrix_sub[leftup[0]][i + 1] = matrix[leftup[0]][i]

        for i in range(leftup[0], rightdown[0] + 1):
            matrix_sub[i + 1][rightdown[1]] = matrix[i][rightdown[1]]

        for i in range(rightdown[1], leftup[1] - 1, -1):
            matrix_sub[rightdown[0]][i - 1] = matrix[rightdown[0]][i]

        for i in range(rightdown[0], leftup[0] - 1, -1):
            matrix_sub[i - 1][leftup[1]] = matrix[i][leftup[1]]

        for i in range(leftup[1], rightdown[1] + 1):
            matrix[leftup[0]][i] = matrix_sub[leftup[0]][i]
            if(matrix_sub[leftup[0]][i] < minValue):
                minValue = matrix_sub[leftup[0]][i]

        for i in range(leftup[0], rightdown[0] + 1):
            matrix[i][rightdown[1]] = matrix_sub[i][rightdown[1]]
            if(matrix_sub[i][rightdown[1]] < minValue):
                minValue = matrix_sub[i][rightdown[1]]

        for i in range(rightdown[1], leftup[1] - 1, -1):
            matrix[rightdown[0]][i] = matrix_sub[rightdown[0]][i]
            if(matrix_sub[rightdown[0]][i] < minValue):
                minValue = matrix_sub[rightdown[0]][i]

        for i in range(rightdown[0], leftup[0] - 1, -1):
            matrix[i][leftup[1]] = matrix_sub[i][leftup[1]]
            if(matrix_sub[i][leftup[1]] < minValue):
                minValue = matrix_sub[i][leftup[1]]

        for i in range(rows + 1):
            print(matrix_sub[i])
        print()
        # for i in range(rows + 2):
        #     print(matrix[i])
        answer.append(minValue)

    for query in queries:
        rotate(query)

    # print(answer)
    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
solution(rows,columns,queries)