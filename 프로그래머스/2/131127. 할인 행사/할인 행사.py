def solution(want, number, discount):
    answer = 0
    dict = {}
    for i in range(len(want)):
        dict[want[i]] = number[i]
    # print(dict)
    tmp_dict = {}
    for key in dict:
        tmp_dict[key] = 0
    for i in range(len(discount)-9):
        tmp_dict = {}
        for key in dict:
            tmp_dict[key] = 0
        for j in range(i, i+10):
            if discount[j] in tmp_dict:
                tmp_dict[discount[j]] += 1
            else:
                tmp_dict[discount[j]] = 1
        # print(tmp_dict)
        flag = 0
        for i in range(len(dict)):
            key = want[i]
            standard = dict[key]
            result = tmp_dict[key]
            if standard > result:
                flag = 0
                break
            else:
                flag = 1
        if flag != 0:
            answer += 1
    return answer