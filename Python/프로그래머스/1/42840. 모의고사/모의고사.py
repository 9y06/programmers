def solution(answers):
    su1 = [1, 2, 3, 4, 5]
    su2 = [2, 1, 2, 3, 2, 4, 2, 5]
    su3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = []
    su1_result = 0
    su2_result = 0
    su3_result = 0
    su1_idx = -1
    su2_idx = -1
    su3_idx = -1
    for j in range(len(answers)):
        su1_idx += 1
        su2_idx += 1
        su3_idx += 1
        if su1_idx >= len(su1):
            su1_idx = 0
        if su2_idx >= len(su2):
            su2_idx = 0
        if su3_idx >= len(su3):
            su3_idx = 0
        if su1[su1_idx] == answers[j]:
            su1_result += 1
        if su2[su2_idx] == answers[j]:
            su2_result += 1
        if su3[su3_idx] == answers[j]:
            su3_result += 1
    result.append(su1_result)
    result.append(su2_result)
    result.append(su3_result)
    answer = []
    for i in range(len(result)):
        if max(result) == result[i]:
            answer.append(i+1)
    return answer