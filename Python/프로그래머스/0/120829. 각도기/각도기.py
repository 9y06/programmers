def solution(angle):
    answer = 0
    if 90 > angle > 0:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 180 > angle > 90:
        answer = 3
    else:
        answer = 4
    return answer