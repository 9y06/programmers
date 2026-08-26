def solution(arr, idx):
    index = idx-1
    for i in arr[idx::]:
        index += 1
        if i == 1:
            return index
    return -1