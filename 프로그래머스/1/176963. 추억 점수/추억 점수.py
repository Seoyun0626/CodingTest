def solution(name, yearning, photo):
    answer = []
    dict = {}
    for i in range(len(name)):
        tmp = name[i]
        num = yearning[i]
        dict[tmp] = num
    # print(dict)
    for j in range(len(photo)):
        cnt = 0
        tmp = photo[j]
        for k in range(len(tmp)):
            name = tmp[k]
            if name in dict:
                cnt += dict[name]
            else:
                continue
        answer.append(cnt)
    # print(answer)
    return answer