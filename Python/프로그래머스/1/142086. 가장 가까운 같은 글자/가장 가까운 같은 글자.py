def solution(s):
    answer = []
    for i in range(len(s)):
        if s[i] not in s[:i]:
            answer.append(-1)
        else:
            cnt = 0
            for j in range(len(s[:i])):
                if s[j] == s[i]:
                    cnt = i - j
            answer.append(cnt)
    return answer