def solution(X, Y):
    answer = ''
    x_dict = {}
    y_dict = {}
    for num in X:
        if num in x_dict:
            x_dict[num] += 1
        else:
            x_dict[num] = 1
    for num in Y:
        if num in y_dict:
            y_dict[num] += 1
        else:
            y_dict[num] = 1
    x_list = list(x_dict)
    y_list = list(y_dict)
    common = [x for x in x_list if x in y_list]
    common.sort(reverse=True)
    # print(common)
    if len(common) == 0:
        answer = "-1"
        return answer
    elif len(common) == 1 and common[0] == "0":
        answer = "0"
        return answer
    else:
        for num in common:
            x_num = x_dict[num]
            y_num = y_dict[num]
            if x_num <= y_num:
                answer += num*x_num
            else:
                answer += num*y_num
    # print(x_dict, y_dict)
    # print(x_list, y_list)
    # print(common)
    return answer