def solution(array, commands):
    answer = []
    for l in range(len(commands)):
        i, j, k = commands[l]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
        arr = []
    return answer