_dict = {}
_list = []

a = [4, 5, 6, 5, 4, 3]

for i in a:
    _dict[i] = 0

for i in a:
    _dict[i] += 1

_sorted = dict(sorted(_dict.items()))

_sorted2 = (sorted(_sorted.items(), key=lambda x: x[1]))

print(_sorted)
print(_sorted2)

for i in _sorted2:
    for j in range(i[1]):
        print(i[0], end=' ')
