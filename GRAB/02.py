def solution(grades):
    answer = []

    arr = {'A+': 0, 'A0': 1, 'A-': 2, 'B+': 3, 'B0': 4, 'B-': 5, 'C+': 6, 'C0': 7, 'C-': 8, 'D+':9, 'D0': 10, 'D-': 11, 'F': 12}

    lecture = {}
    for i, grade in enumerate(grades):
        subject, score = grade.split()
        if subject not in lecture.keys():
            lecture[subject] = (score, i)
        else:
            if arr[lecture[subject][0]] > arr[score]:
                lecture[subject] = (score, i)

    for key in lecture.keys():
        answer.append(key + ' ' + lecture[key][0])
    # print(lecture)
    answer = sorted(answer, key=lambda x: (arr[x.split()[1]], lecture[x.split()[0]][1]))
    # print(answer)

    return answer

grades = ["DM0106 D-", "PL6677 B+", "DM0106 B+", "DM0106 B+", "PL6677 C0", "GP0000 A0"]
solution(grades)