def solution(numbers):
    num_set = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
    answer = set(num_set) - set(numbers)
    return sum(answer)