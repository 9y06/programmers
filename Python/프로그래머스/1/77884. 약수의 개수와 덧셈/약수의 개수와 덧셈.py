def solution(left, right):
    answer = 0
    result = 0
    for i in range(left, right+1):
        for j in range(1, i+1):
            if i % j == 0:
                answer += 1
        if answer % 2 == 0:
            result += i
        else:
            result -= i
        answer = 0
    return result