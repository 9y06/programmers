def solution(seoul):
    answer = ''
    for i in seoul:
        if i == "Kim":
            location = seoul.index("Kim")
    answer = f"김서방은 {location}에 있다"
    return answer