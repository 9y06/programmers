def solution(n):
    li = list(str(n))
    li.sort(reverse=True)
    answer = ''
    for i in li:
        answer += i
    return int(answer)