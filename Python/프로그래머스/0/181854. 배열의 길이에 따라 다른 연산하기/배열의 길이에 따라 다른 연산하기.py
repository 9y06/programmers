def solution(arr, n):
    cnt = len(arr)
    if cnt % 2 == 1:
        for i in range(0, cnt, 2):
            arr[i] += n
    else:
        for i in range(1, cnt, 2):
            arr[i] += n
    return arr