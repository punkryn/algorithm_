# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(record):
    answer = []

    userid = dict()

    for i, r in enumerate(record):
        string = r.split()
        if len(string) == 3:
            action, uid, nick = string
        else:
            action, uid = string

        if action == 'Change':
            userid[uid][-1] = nick

        if uid not in userid.keys():
            # userid[uid] = [nick]
            # userid[uid].append({i: action})
            userid[uid] = {-1: nick}
            userid[uid][i] = action
        else:
            if action == 'Enter':
                userid[uid][-1] = nick
            userid[uid][i] = action
        #print(userid)

    #print(userid)

    for i, r in enumerate(record):
        string = r.split()
        if len(string) == 3:
            action, uid, nick = string
        else:
            action, uid = string

        nick = userid[uid][-1]
        action = userid[uid][i]

        if action == 'Enter':
            answer.append(nick + '님이 들어왔습니다.')
        elif action == 'Leave':
            answer.append(nick + '님이 나갔습니다.')

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))