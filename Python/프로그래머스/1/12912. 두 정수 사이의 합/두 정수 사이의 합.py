def solution(a, b):
    answer = 0
    li = [a, b]
    for i in range(min(li), max(li)+1):
        answer += i
    return answer