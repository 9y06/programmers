def solution(d, budget):
    answer = 0
    d.sort()
    b = 0
    for i in d:
        if answer + i > budget:
            pass
        else:
            answer += i
            b += 1
    return b