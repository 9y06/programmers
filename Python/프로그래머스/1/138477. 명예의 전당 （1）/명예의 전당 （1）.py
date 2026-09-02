def solution(k, score):
    answer = []
    li = []
    for i in score:
        answer.append(i)
        answer.sort(reverse=True)
        if len(answer) >= k:
            del answer[k:]
        li.append(min(answer))
    return li