def solution(dartResult):
    score = []
    num_li = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    i = 0
    num = 0
    while i < len(dartResult):
        if dartResult[i:i+2] == '10':
            num = 10
            i += 2
        # elif dartResult[i] in num_li:
        else:
            num = int(dartResult[i])
            i += 1
        
        if dartResult[i] == 'S':
            i += 1
        elif dartResult[i] == 'D':
            num = num ** 2
            i += 1
        elif dartResult[i] == 'T':
            num = num ** 3
            i += 1
        
        if i < len(dartResult) and dartResult[i] == '*':
            num = num * 2
            if score:
                score[-1] = score[-1] * 2
            i += 1
        elif i < len(dartResult) and dartResult[i] == '#':
            num = num * -1
            i += 1
        score.append(num)
    return sum(score)