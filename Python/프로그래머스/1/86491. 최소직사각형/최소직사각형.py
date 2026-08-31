def solution(sizes):
    min_li = []
    max_li = []
    for i in sizes:
        min_li.append(min(i))
        max_li.append(max(i))
    return max(min_li) * max(max_li)