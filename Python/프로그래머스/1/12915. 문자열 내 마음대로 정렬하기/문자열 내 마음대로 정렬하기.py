def solution(strings, n):
    answer = []
    li = []
    for i in strings:
        li.append(i[n]+i)
    li.sort()
    for i in range(len(li)):
        answer.append(li[i][1:])
    return answer