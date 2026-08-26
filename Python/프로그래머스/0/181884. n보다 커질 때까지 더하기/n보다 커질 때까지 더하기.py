def solution(numbers, n):
    answer = []
    for i in numbers:
        answer.append(i)
        if sum(answer) > n:
            return sum(answer)