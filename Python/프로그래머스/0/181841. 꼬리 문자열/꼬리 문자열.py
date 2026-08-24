def solution(str_list, ex):
    answer = []
    for i in str_list:
        answer.append(i)
        if ex in i:
            answer.remove(i)
    return "".join(answer)