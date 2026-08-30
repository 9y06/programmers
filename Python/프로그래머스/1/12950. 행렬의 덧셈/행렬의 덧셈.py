def solution(arr1, arr2):
    answer2 = []
    arr_len = len(arr1)
    x = len(arr1[0])
    for i in range(arr_len):
        answer1 = []
        for j in range(x):
            answer1.append(arr1[i][j] + arr2[i][j])
        answer2.append(answer1)
    return answer2