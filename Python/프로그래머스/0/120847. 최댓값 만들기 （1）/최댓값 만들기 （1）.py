def solution(numbers):
    answer = 0
    fir_max = max(numbers)
    numbers.remove(max(numbers))
    sec_max = max(numbers)
    answer = fir_max*sec_max
    return answer