def solution(phone_number):
    li = list(phone_number)
    for i in range(len(li)-4):
        li[i] = "*"
    return ''.join(li)