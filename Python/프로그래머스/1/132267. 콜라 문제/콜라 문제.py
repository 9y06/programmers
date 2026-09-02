def solution(a, b, n):
    coke = 0
    while n >= a:
        cnt = n // a
        coke += cnt * b
        n = n % a + cnt * b
    return coke