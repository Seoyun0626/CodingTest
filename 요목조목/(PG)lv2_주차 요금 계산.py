import math
# fees = [180, 5000, 10, 600]
# records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
in_dic = {}
out_dic = {}
total_dic = {}
answer = []

for i in range(len(records)):
    time, num, state = map(str, records[i].split())
    hour, minute = map(int, time.split(":"))
    total_time = hour * 60 + minute
    if num not in in_dic:
        in_dic[num] = total_time
    else:
        if num not in total_dic:
            total_dic[num] = total_time - in_dic[num]
            del in_dic[num]
        else:
            total_dic[num] += total_time - in_dic[num]
            del in_dic[num]
    # print(in_dic, "in_dic")
if len(in_dic) != 0:
    for key, value in in_dic.items():
        if key not in total_dic:
            total_dic[key] = 23 * 60 + 59 - value
        else:
            total_dic[key] += 23 * 60 + 59 - value
# print(total_dic)
total_dic = sorted(total_dic.items() , key = lambda x : x[0])
# print(total_dic)

for i in range(len(total_dic)):
    money = 0
    if total_dic[i][1] <= fees[0]:
        answer.append(fees[1])
    else:
        money = fees[1] + math.ceil((total_dic[i][1] - fees[0]) / fees[2]) * fees[3]
        answer.append(money)
print(answer)


