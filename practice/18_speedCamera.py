# https://programmers.co.kr/learn/courses/30/lessons/42884

def solution(routes):
    answer = 0

    routes.sort(key=lambda x: x[1])

    camera = -30001

    for route in routes:
        if camera < route[0]:
            camera = route[1]
            answer += 1

    # bar = routes[0][1]
    #
    # # inCamera = [[x, y] for x, y in routes if x <= bar <= y]
    # notInCamera = [[x, y] for x, y in routes if bar < x]
    # answer += 1
    #
    # while notInCamera:
    #     notInCamera.sort(key=lambda x: x[1])
    #     bar = notInCamera[0][1]
    #     notInCamera = [[x, y] for x, y in routes if bar < x]
    #     answer += 1

    return answer

routes = [[-20,15], [-14,-5], [-18,-13], [-5,-3]]
print(solution(routes))