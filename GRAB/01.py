def solution(infos, actions):
    answer = []

    user = {}
    for info in infos:
        tmp = info.split()
        user[tmp[0]] = tmp[1]

    isLogon = False
    backet = []
    for action in actions:
        # print(action)
        act = action.split()
        if act[0] == 'LOGIN':
            if isLogon:
                answer.append(False)
                continue
            id = act[1]
            pwd = act[2]
            if id in user.keys():
                if pwd == user[id]:
                    isLogon = True
                    answer.append(True)
                else:
                    answer.append(False)
            else:
                answer.append(False)

        elif act[0] == 'ADD':
            # print(act)
            if isLogon:
                food = act[1]
                backet.append(food)
                answer.append(True)
            else:
                answer.append(False)
                # continue
        elif act[0] == 'ORDER':
            if backet:
                # print(backet)
                answer.append(True)
                backet = []
            else:
                # print(backet, isLogon)
                answer.append(False)
                # continue


    # print(answer)
    return answer