from itertools import combinations
def solution(numbers):
    answer = []
    li = combinations(numbers, 2)
    for i in li:
        if sum(i) not in answer:
            answer.append(sum(i))
    answer.sort()
    return answer