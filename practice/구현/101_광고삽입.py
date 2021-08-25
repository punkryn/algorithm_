# https://programmers.co.kr/learn/courses/30/lessons/72414#fn1
# https://dev-note-97.tistory.com/156

def solution(play_time, adv_time, logs):
    answer = ''

    logs_start_sec = [0] * len(logs)
    logs_end_sec = [0] * len(logs)

    pts = play_time.split(":")
    play_time_sec = int(pts[0]) * 3600 + int(pts[1]) * 60 + int(pts[2])

    ats = adv_time.split(":")
    adv_time_sec = int(ats[0]) * 3600 + int(ats[1]) * 60 + int(ats[2])

    for i in range(len(logs)):
        ls = logs[i].split("-")
        startsp = ls[0].split(":")
        endsp = ls[1].split(":")

        logs_start_sec[i] = int(startsp[0]) * 3600 + int(startsp[1]) * 60 + int(startsp[2])
        logs_end_sec[i] = int(endsp[0]) * 3600 + int(endsp[1]) * 60 + int(endsp[2])

    total_time = [0] * (play_time_sec + 1)

    for i in range(len(logs)):
        total_time[logs_start_sec[i]] = total_time[logs_start_sec[i]] + 1
        total_time[logs_end_sec[i]] = total_time[logs_end_sec[i]] - 1

    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]

    most_view = 0
    max_time = 0
    print(adv_time_sec, play_time_sec)
    print(total_time[adv_time_sec - 1: play_time_sec])
    for i in range(adv_time_sec - 1, play_time_sec):
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i - adv_time_sec]:
                most_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1

    h = max_time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    max_time %= 3600

    m = max_time // 60
    m = '0' + str(m) if m < 10 else str(m)
    max_time %= 60

    s = '0' + str(max_time) if max_time < 10 else str(max_time)

    answer = h + ':' + m + ':' + s
    return answer

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))
