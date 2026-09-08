def solution(number, limit, power):
    li = []
    answer = 0
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(i**0.5)+1):
            if i % j == 0:
                cnt += 1
                if i % (i // j) == 0 and j != i // j:
                    cnt += 1
        li.append(cnt)
    for i in li:
        if i > limit:
            answer += power
        else:
            answer += i
    return answer