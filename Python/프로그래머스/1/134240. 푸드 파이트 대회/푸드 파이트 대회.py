def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] >= 2:
            answer += str(i) * (food[i]//2)
    answer += "0"
    s = answer[-2::-1]
    answer += s
    return answer