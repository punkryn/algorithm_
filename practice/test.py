from itertools import permutations
import copy

def check(password, user):
    global count
    hit = 0
    miss = 0

    for i in range(len(password)):
        for j in range(len(user)):
            if i == j and password[i] == user[j]:
                hit += 1
            elif i != j and password[i] == user[j]:
                miss += 1

    count += 1
    return hit, miss

count = 0
password = [5, 8, 7, 6]
user = [4, 1, 3, 9]

hit, miss = check(password, user)
print(hit, miss)

number = list((i) for i in range(10))
ans = 0
flag = False
answer = [-1] * 4
number_index = [[1] * 4 for _ in range(10)]
bound = 4
while hit != 4:
    print(count, hit + miss)
    if hit + miss == 0:
        for w in user:
            if w in number:
                number.remove(w)
            number_index[w] = [0, 0, 0, 0]
            # print(number_index)
        user = number[:4]
        print(user)
    elif hit + miss == bound:
        for per in permutations(answer, 4):
            hit, miss = check(password, per)
            if hit == 4:
                flag = True
                break

    else:
        if hit == 1:
            for i in range(4):
                user_ = copy.deepcopy(user)
                tmp = [0, 1, 2, 3]
                tmp.remove(i)
                pre = user_[tmp[0]]
                for t in range(1, len(tmp)):
                    user_[tmp[t - 1]] = user_[tmp[t]]
                user_[tmp[-1]] = pre
                print('user_', user_)

                hit, miss = check(password, user_)
                if hit == 0:
                    for j in range(4):
                        number_index[user_[j]][j] = 0

                print(number_index)

            for i in range(4):
                user_ = copy.deepcopy(user)
                tmp = [0, 1, 2, 3]
                tmp.remove(i)
                #pre = user_[tmp[-1]]
                now = user_[tmp[0]]
                for t in range(len(tmp) - 1):
                    nexts = user_[tmp[t + 1]]
                    user_[tmp[t + 1]] = now
                    now = nexts
                user_[tmp[0]] = now
                print('user_2', user_)

                hit, miss = check(password, user_)
                if hit == 0:
                    for j in range(4):
                        number_index[user_[j]][j] = 0

                print(number_index)

        elif hit == 2:
            for i in range(3):
                for j in range(i + 1, 4):
                    user_ = copy.deepcopy(user)
                    tmp = [0, 1, 2, 3]
                    tmp.remove(i)
                    tmp.remove(j)

                    pre = user_[tmp[0]]
                    for t in range(1, len(tmp)):
                        user_[tmp[t - 1]] = user_[tmp[t]]
                    user_[tmp[-1]] = pre
                    print('user_', user_)

                    hit, miss = check(password, user_)
                    if hit == 0:
                        for j in range(4):
                            number_index[user_[j]][j] = 0

            for i in range(3):
                for j in range(i + 1, 4):
                    user_ = copy.deepcopy(user)
                    tmp = [0, 1, 2, 3]
                    tmp.remove(i)
                    tmp.remove(j)
                    # pre = user_[tmp[-1]]
                    now = user_[tmp[0]]
                    for t in range(len(tmp) - 1):
                        nexts = user_[tmp[t + 1]]
                        user_[tmp[t + 1]] = now
                        now = nexts
                    user_[tmp[0]] = now
                    print('user_2', user_)

                    hit, miss = check(password, user_)
                    if hit == 0:
                        for j in range(4):
                            number_index[user_[j]][j] = 0

        elif hit == 3:
            for i in range(4):
                user_ = copy.deepcopy(user)
                tmp = [0, 1, 2, 3]
                now = user_[i]
                tmp.remove(i)
                for j in range(10):
                    if number_index[j][i] == 1 and j != now and j not in user_:
                        user_[i] = j
                        break

                hit, miss = check(password, user_)
                if hit == 3:
                    for t in tmp:
                        for j in range(4):
                            if j != t:
                                number_index[user_[t]][j] = 0
                elif hit == 4:
                    for k, t in enumerate(user_):
                        for j in range(4):
                            if k != j:
                                number_index[t][j] = 0

        for j in range(10):
            one_count = 0
            one_index = 5
            for k in range(4):
                if number_index[j][k] == 1:
                    one_count += 1
                    one_index = k

            if one_count == 1:
                answer[one_index] = j

        for i in range(4):
            if answer[i] != -1:
                bound -= 1

        for i in range(4):
            if answer[i] == -1:
                for j in range(10):
                    if number_index[j][i] == 1 and j not in answer:
                        answer[i] = j

        user = answer

    print('ans', answer)

    if flag:
        break
    hit, miss = check(password, user)
print(count)