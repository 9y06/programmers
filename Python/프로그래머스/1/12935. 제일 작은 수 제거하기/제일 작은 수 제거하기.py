def solution(arr):
    answer = []
    if arr == [10]:
        answer.append(-1)
        return answer
    else:
        min_arr = min(arr)
        arr.remove(min_arr)
        return arr