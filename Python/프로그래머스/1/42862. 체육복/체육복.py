def solution(n, lost, reserve):
    for i in range(1, n+1):
        if i in reserve and i in lost:
            reserve.remove(i)
            lost.remove(i)
            
    reserve.sort()
    lost.sort()
    
    for i in lost:
        if i - 1 in reserve:
            reserve.remove(i-1)
        elif i + 1 in reserve:
            reserve.remove(i+1)
        else:
            n -= 1
    
    return n