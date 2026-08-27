def solution(my_strings, parts):
    answer = []
    cnt = -1
    for i in my_strings:
        cnt += 1
        a, b = parts[cnt]
        answer += my_strings[cnt][a:b+1]
    return ''.join(answer)