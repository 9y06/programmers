def solution(nums):
    can = int(len(nums)/2)
    phone = len(set(nums))
    return min(phone, can)