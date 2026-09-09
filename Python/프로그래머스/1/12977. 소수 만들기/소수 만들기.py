from itertools import combinations

def solution(nums):
    li = list(combinations(nums, 3))
    num = len(li)
    for i in li:
        for j in range(2, int(sum(i)**0.5)+1):
            if sum(i) % j == 0:
                num -= 1
                break
    return num