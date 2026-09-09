def solution(lottos, win_nums):
    answer = []
    zero = 0
    win = 0
    for i in lottos:
        if i == 0:
            zero += 1
        else:
            if i in win_nums:
                win += 1
    if win + zero == 6:
        answer.append(1)
    elif win + zero == 5:
        answer.append(2)
    elif win + zero == 4:
        answer.append(3)
    elif win + zero == 3:
        answer.append(4)
    elif win + zero == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if win == 6:
        answer.append(1)
    elif win == 5:
        answer.append(2)
    elif win == 4:
        answer.append(3)
    elif win == 3:
        answer.append(4)
    elif win == 2:
        answer.append(5)
    else:
        answer.append(6)

    return answer