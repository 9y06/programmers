def solution(my_string, n):
    answer = ''
    str_li = list(my_string)[:n]
    for i in str_li:
        answer += i
    return answer