def solution(k, score):
    answer = []
    li = []
    for i in score:
        li.append(i)
        li.sort(reverse=True)
        myeong = li[:k]
        answer.append(myeong[-1])
    return answer