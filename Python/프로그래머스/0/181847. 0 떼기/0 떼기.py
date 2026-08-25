def solution(n_str):
    for i in n_str:
        if i != "0":
            return n_str[n_str.index(i):]