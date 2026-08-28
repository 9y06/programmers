def solution(x):
    # answer = True
    x_sum = sum([int(x) for x in str(x)])
    if x % x_sum == 0:
        return True
    else:
        return False