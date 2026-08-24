def solution(my_string):
    answer = ''
    moum = ["a", "e", "i", "o", "u"]
    for i in my_string:
        if i in moum:
            pass
        else:
            answer += i
    return answer