def solution(d, budget):
    cnt = 0
    
    
    d.sort()


    for i in range(len(d)):
        if budget // d[i] != 0:
            cnt += 1
            budget -= d[i]
        else:
            break
    return cnt