def solution(n, lost, reserve):
    import copy
    new_lost = copy.deepcopy(lost)

    dic = {}
    cnt = n - len(lost)
    for i in range(1, n + 1):
        if i in reserve:
            dic[i] = 1
        else:
            dic[i] = 0

    for i in range(len(new_lost)):
        for y in reserve:
            if new_lost[i] == y:
                cnt += 1
                lost.remove(new_lost[i])
                dic[new_lost[i]] = 0
    lost = sorted(lost)
    for x in lost:
        flag = 0
        if x == 1:
            if dic[2]:
                cnt += 1
                dic[2] = 0
        elif x < n:
            if dic[x - 1]:
                cnt += 1
                dic[x - 1] = 0
                flag = 1
            elif dic[x + 1] and flag == 0:
                cnt += 1
                dic[x + 1] = 0
        else:
            if dic[x - 1]:
                cnt += 1

    return cnt