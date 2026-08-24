def solution(strlist):
    answer = []
    for i in strlist:
        str_num = 0
        for j in i:
            str_num += 1
        answer.append(str_num)
    return answer