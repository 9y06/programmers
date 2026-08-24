def solution(n):
    answer = 0
    n_li = list(str(n))
    for i in n_li:
        answer += int(i)
    return answer