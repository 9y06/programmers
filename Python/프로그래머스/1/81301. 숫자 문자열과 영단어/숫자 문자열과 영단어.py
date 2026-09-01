def solution(s):
    answer = ""
    num= ""
    alpha = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in range(len(s)):
        num += str(s[i])
        if num in list(alpha.values()):
            answer += num
            num = ""
        elif num in list(alpha.keys()):
            answer += alpha[num]
            num = ""
    return int(answer)