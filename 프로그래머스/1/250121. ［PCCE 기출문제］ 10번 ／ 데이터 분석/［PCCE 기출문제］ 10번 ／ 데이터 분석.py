def solution(data, ext, val_ext, sort_by):
    answer = []
    for i in range(len(data)):
        tmp = data[i]
        if ext == "code" and tmp[0] < val_ext:
            answer.append(tmp)
        if ext == "date" and tmp[1] < val_ext:
            answer.append(tmp)
        if ext == "maximum" and tmp[2] < val_ext:
            answer.append(tmp)
        if ext == "remain" and tmp[3] < val_ext:
            answer.append(tmp)
    print(answer)
    if sort_by == "code":
        answer.sort(key=lambda x:x[0])
    if sort_by == "date":
        answer.sort(key=lambda x:x[1])
    if sort_by =="maximum":
        answer.sort(key=lambda x:x[2])
    if sort_by == "remain":
        answer.sort(key=lambda x:x[3])
    return answer