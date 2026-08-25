def solution(binomial):
    answer = []
    answer = binomial.split(" ")
    a = answer[0]
    op = answer[1]
    b = answer[2]
    if op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)
    else:
        return int(a) * int(b)
