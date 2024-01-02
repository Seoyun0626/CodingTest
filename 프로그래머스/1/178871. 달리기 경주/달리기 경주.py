def solution(players, callings):
    dic = {}
    for i in range(len(players)):
        name = players[i]
        dic[name] = i+1
    convert_dic = {v:k for k,v in dic.items()} 
    # print(dic)
    # print(convert_dic)
    for j in range(len(callings)):
        name = callings[j]
        cur_num = dic[name]
        loser_name = convert_dic[cur_num-1]
        convert_dic[cur_num-1] = name
        convert_dic[cur_num] = loser_name
        dic[name] = cur_num-1
        dic[loser_name] = cur_num
        # print(convert_dic)
    answer = []
    for key, value in convert_dic.items():
        answer.append(value)
    return answer