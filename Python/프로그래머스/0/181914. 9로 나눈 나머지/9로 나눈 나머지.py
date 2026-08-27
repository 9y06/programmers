def solution(number):
    answer = sum(int(x) for x in list(number))
    return answer % 9