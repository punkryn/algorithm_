from itertools import permutations


def hit(l1, l2):
    global ll
    ll += 1
    cnt = 0
    for i in range(len(l1)):
        if l1[i] == l2[i]:
            cnt += 1
    return cnt


def miss(guess, l2):
    cnt = 0
    for number in l2:
        if number in guess:
            cnt += 1
    cnt -= hit(guess, l2)
    return cnt


def solution(guess):
    number = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    _list = []
    realidx = [0, 0, 0, 0]
    for _ in range(4):
        _list.append(number.pop())
    total_count = 0
    print(_list, number)

    print('hit : ', hit(guess, _list), '\nmiss : ', miss(guess, _list))
    h = hit(guess, _list)
    m = miss(guess, _list)
    total_count += 1

    while number:
        npop = number.pop()

        for i in range(4):
            previous_h = hit(guess, _list)
            previous_m = miss(guess, _list)
            if realidx[i] == 0:
                current_num = _list[i]
                _list[i] = npop

                print('hit : ', hit(guess, _list), '\nmiss : ', miss(guess, _list), '\n_list : ', _list)
                h = hit(guess, _list)
                m = miss(guess, _list)
                total_count += 1

                print('hit, pre', h, previous_h)

                if h > previous_h:
                    realidx[i] = 1
                    continue
                if h < previous_h:
                    realidx[i] = 1
                    _list[i] = current_num
                    continue
                _list[i] = current_num

    print(guess, _list, h, m, realidx)

    check = []
    searchplz = []
    for idx, r in enumerate(realidx):
        if r == 1:
            check.append([idx, _list[idx]])
        else:
            searchplz.append(idx)
    cnt = 0
    print('realidx', realidx)
    print('check2', check)
    print('_list', _list)
    for per in list(permutations(_list)):
        print('per', per, check)
        for idx, c in check:
            #print('123123')
            if per[idx] == c:
                cnt += 1

        if cnt == len(check):
            print('hit : ', hit(guess, per), '\nmiss : ', miss(guess, per), '\n_list : ', per)
            h = hit(guess, per)
            m = miss(guess, per)
            total_count += 1
            if h == 4:
                print(guess, per, h, m, total_count)
                print('en2')
                return per
            cnt = 0
        else:
            cnt = 0

    ran = list(range(0, 10))
    print('check', check)
    for idx, c in check:
        for r in ran:
            if r == c:
                ran.remove(r)
    print('ran', ran)
    print('search', searchplz)
    for r in ran:
        for se in searchplz:
            _list[se] = r
            print('hit : ', hit(guess, _list), '\nmiss : ', miss(guess, _list), '\n_list : ', _list)
            h = hit(guess, _list)
            m = miss(guess, _list)
            total_count += 1
            if h == 4:
                print(guess, _list, h, m, total_count)
                print('end')
                return _list
            # else:

    print(guess, _list, h, m, total_count)

ll = 0
guess = '8975'
guess = list(map(int, list(guess)))
print(solution(guess))
print(ll)
