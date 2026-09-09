def solution(players, callings):
    p = {}
    for i in range(len(players)):
        p[players[i]] = i
    for i in callings:
        idx = p[i]
        front = players[idx-1]        # 앞사람 이름 기억

        players[idx-1], players[idx] = players[idx], players[idx-1]

        p[i] = idx - 1                # 부른 사람은 한 칸 앞으로
        p[front] = idx                # 앞사람은 한 칸 뒤로
    return players