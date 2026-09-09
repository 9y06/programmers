def solution(numbers, hand):
    answer = ''
    def pos(n):
        if n == '*':
            return (3, 0)
        elif n == 0:
            return (3, 1)
        elif n == '#':
            return (3, 2)
        else:
            return ((n-1)//3, (n-1)%3)
    def dis(a, b):
        return (abs(a[0]-b[0])+abs(a[1]-b[1]))
    left = pos('*')
    right = pos('#')
    for i in numbers:
        if i in (1, 4, 7):
            left = pos(i)
            answer += 'L'
        elif i in (3, 6, 9):
            right = pos(i)
            answer += 'R'
        else:
            dr = dis(right, pos(i))
            dl = dis(left, pos(i))
            if dr > dl:
                left = pos(i)
                answer += 'L'
            elif dl > dr:
                right = pos(i)
                answer += 'R'
            else:
                if hand == 'right':
                    right = pos(i)
                    answer += 'R'
                elif hand == 'left':
                    left = pos(i)
                    answer += 'L'
    return answer