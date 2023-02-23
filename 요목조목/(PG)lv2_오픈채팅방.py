record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
info_dic = {}
result = []
answer = []
for i in range(len(record)):
    if record[i][0] == "E":
        action, user_id, name = map(str, record[i].split())
        info_dic[user_id] = name
        tmp = user_id + '님이 들어왔습니다.'
        result.append(tmp)
        # print(action, user_id, name)
    elif record[i][0] == "L":
        action, user_id = map(str, record[i].split())
        tmp = user_id + '님이 나갔습니다.'
        result.append(tmp)
        # print(action, user_id)
    else:
        action, user_id, name = map(str, record[i].split())
        info_dic[user_id] = name
        # print(action, user_id, name)
# print(result)
# print(info_dic)

for i in range(len(result)):
    first, last = map(str, result[i].split("님"))
    first = info_dic[first]
    tmp = first + '님' + last
    answer.append(tmp)
print(answer)
