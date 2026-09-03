def solution(a, b):
    answer = ''
    day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date = [ "FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    answer = date[(sum(day[:a-1])+b)%7-1]
    return answer