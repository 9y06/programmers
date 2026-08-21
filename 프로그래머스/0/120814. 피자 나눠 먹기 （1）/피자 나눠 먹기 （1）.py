import math
def solution(n):
    if n > 7:
        answer = math.ceil(n//7) + math.ceil(n%7/7)
    else:
        answer = 1
    return answer