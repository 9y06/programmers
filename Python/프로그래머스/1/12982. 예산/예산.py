def solution(d, budget):
    answer = 0
    cnt = 0
    d.sort()
    for i in d:
        if answer <= budget:
            if answer + i > budget:
                pass
            else:
                answer += i
                cnt += 1
    return cnt