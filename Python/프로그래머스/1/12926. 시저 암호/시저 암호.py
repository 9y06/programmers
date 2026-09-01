def solution(s, n):
    answer = ''
    for i in s:
        if i == " ":
            answer += i
        else:
            for j in range(n):
                if ord(i) == ord("z"):
                    i = "a"
                elif ord(i) == ord("Z"):
                    i = "A"
                else:
                    i = chr(ord(i) + 1)
            answer += chr(ord(i))
    return answer