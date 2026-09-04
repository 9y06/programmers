def solution(n, m, section):
    answer = 0
    painted_end = 0
    for i in section:
        if i > painted_end:
            answer += 1
            painted_end = i + m - 1
    return answer