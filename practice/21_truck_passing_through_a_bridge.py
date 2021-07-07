# https://programmers.co.kr/learn/courses/30/lessons/42583

def solution(bridge_length, weight, truck_weights):
    answer = 0
    passed = []
    passing = []

    time = 0
    while truck_weights:
        time += 1
        # print(passing, time)
        for t in passing:
            t[1] += 1

        if passing:
            if passing[0][1] == bridge_length:
                passed.append(passing.pop(0))

        svalue = 0
        for a in passing:
            svalue += a[0]
        if svalue + truck_weights[0] <= weight and len(passing) + 1 <= bridge_length:
            truck = truck_weights.pop(0)
            passing.append([truck, 0])
    # print(time, passing)
    time += (bridge_length - passing[-1][1])

    answer = time

    return answer

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))