def solution(my_string):
    answer = 0
    li = []
    for i in my_string:
        li.append(i)
        
    for i in li:
        if str.isdigit(i) == True:
            answer += int(i)
        else:
            pass
    return answer