def solution(myString):
    stringList = myString.split("x")
    answer = []
    for i in stringList:
        answer.append(len(i))
    return answer