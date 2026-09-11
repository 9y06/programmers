def solution(food):
    answer = ''
    for i in range(len(food)):
        if food[i] // 2 > 0:
            answer += str(i)*(food[i]//2)
    n = answer[::-1]
    answer += '0'
    answer += n
    return answer