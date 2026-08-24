def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n // i == i and n % i == 0:
            answer = 1
    if answer == 0:
        answer = 2
    return answer