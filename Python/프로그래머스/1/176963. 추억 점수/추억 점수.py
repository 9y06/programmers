def solution(name, yearning, photo):
    answer = []
    for i in photo:
        cnt = 0
        for j in i:
            if j in name:
                cnt += yearning[name.index(j)]
        if cnt == 0:
            answer.append(0)
        else:
            answer.append(cnt)
    return answer