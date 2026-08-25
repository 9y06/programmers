def solution(strArr):
    answer = []
    j = 0
    for i in strArr:
        if j % 2 == 1:
            answer.append(i.upper())
            j += 1
        else:
            answer.append(i.lower())
            j += 1
    return answer