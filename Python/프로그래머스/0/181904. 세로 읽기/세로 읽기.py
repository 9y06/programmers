def solution(my_string, m, c):
    answer = ''
    a = ''
    cnt = 0
    for i in my_string:
        cnt += 1
        a += i
        if cnt >= m:
            answer += a[c-1]
            cnt = 0
            a = ""
    return answer