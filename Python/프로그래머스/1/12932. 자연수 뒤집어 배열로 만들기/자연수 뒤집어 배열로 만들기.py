def solution(n):
    answer = [int(x) for x in str(n)]
    li = []
    for i in range(len(answer)-1, -1, -1):
        li.append(answer[i])
    return li