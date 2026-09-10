def solution(s, skip, index):
    answer = ''
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in skip:
        alpha.remove(i)
    li_len = len(alpha)
    for i in s:
        next_idx = (alpha.index(i) + index) % li_len
        answer += alpha[next_idx]
    return answer