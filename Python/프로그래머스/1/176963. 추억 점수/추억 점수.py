def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        num = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                num += yearning[name.index(photo[i][j])]
        answer.append(num)
    return answer