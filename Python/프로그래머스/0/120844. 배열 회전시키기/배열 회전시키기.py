def solution(numbers, direction):
    if direction == "right":
        item = numbers.pop(-1)
        numbers.insert(0, item)
    else:
        item = numbers.pop(0)
        numbers.insert(len(numbers), item)
    return numbers