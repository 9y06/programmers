def solution(s):
    answer = []
    cnt = 0
    
    for i in s:
        if i == " ":
            answer.append(i)
            cnt = 0
        else:
            if cnt % 2 == 0:
                answer.append(i.upper())
                cnt += 1
            else:
                answer.append(i.lower())
                cnt +=1
                
    return "".join(answer)