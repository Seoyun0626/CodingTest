def solution(cards1, cards2, goal):
    answer = ''
    flag = 0
    for word in goal:
        if len(cards1) > 0:
            if word == cards1[0]:
                del cards1[0]
                continue
        if len(cards2) > 0:
            if word == cards2[0]:
                del cards2[0]
                continue
        flag = 1
        break
    if flag == 1:
        answer += "No"
    else:
        answer += "Yes"
    return answer