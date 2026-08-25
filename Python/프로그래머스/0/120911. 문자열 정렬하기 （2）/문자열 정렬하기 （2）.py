def solution(my_string):
    my_string = my_string.lower()
    my_string = list(my_string)
    my_string.sort()
    answer = "".join(i for i in my_string)
    return answer