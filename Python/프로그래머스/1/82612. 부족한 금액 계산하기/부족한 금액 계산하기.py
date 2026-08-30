def solution(price, money, count):
    answer = 0
    cost = 0
    for i in range(1, count+1):
        cost += price * i
    if cost <= money:
        return 0
    else:
        return abs(cost - money)