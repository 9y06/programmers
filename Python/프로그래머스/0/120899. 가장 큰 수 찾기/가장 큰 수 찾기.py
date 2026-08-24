def solution(array):
    answer = []
    max_int = 0
    for i in array:
        if i > max_int:
            max_int = i
    answer = [max_int, array.index(max_int)]
    return answer