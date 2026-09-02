def solution(nums):
    answer = []
    n = len(nums) // 2
    for i in nums:
        if i in answer:
            pass
        else:
            if len(answer) >= n:
                return len(answer)
            else:
                answer.append(i)
    return len(answer)