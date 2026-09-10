def solution(n):
    answer = [True] * (n+1)
    answer[0] = answer[1] = False
    for i in range(len(answer)):
        if answer[i]:
            for j in range(i*i, len(answer), i):
                answer[j] = False
    return sum(answer)