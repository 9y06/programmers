def solution(my_string, num1, num2):
    my_string = list(my_string)
    num1_str = my_string[num1]
    num2_str = my_string[num2]
    my_string[num1] = num2_str
    my_string[num2] = num1_str
    return ''.join(my_string)