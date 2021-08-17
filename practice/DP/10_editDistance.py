def show(edit):
    for i in range(len(edit)):
        for j in range(len(edit)):
            print(edit[i][j], end=' ')
        print()
    print()

a = 'sunday'
b = 'saturday'

edit = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a) + 1):
    edit[i][0] = i
for i in range(len(b) + 1):
    edit[0][i] = i

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        edit[i][j] = min(edit[i - 1][j] + 1, edit[i][j - 1] + 1, edit[i - 1][j - 1] + 1 if a[i - 1] != b[j - 1] else edit[i - 1][j - 1])

print(edit[len(a)][len(b)])