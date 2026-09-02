def solution(n, arr1, arr2):
    answer1 = []
    answer2 = []
    li = ['']*n
    for i in arr1:
        answer1.append(bin(i)[2:].zfill(n))
    for i in arr2:    
        answer2.append(bin(i)[2:].zfill(n))
    for i in range(n):
        for j in range(n):
            if answer1[i][j] == answer2[i][j]:
                if answer1[i][j] == "1":
                    li[i] += "#"
                else:
                    li[i] += " "
            elif answer1[i][j] == "1" or answer2[i][j] == "1":
                li[i] += "#"
            else:
                li[i] += " "
    return li