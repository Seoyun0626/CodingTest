def solution(absolutes, signs):
    total = []
    for i in range(len(absolutes)):
        if signs[i]:
            total.append(absolutes[i])
        else:
            total.append((-1) * absolutes[i])
        
    return sum(total)