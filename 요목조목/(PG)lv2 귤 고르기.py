# k = 6
# tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
result = 1
# k = 4
# tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]
cnt = 0
dic = {}

for i in tangerine:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
# print(dic)
new_dic = sorted(dic.items(), key = lambda x : x[1], reverse=True)
# print(new_dic)


for i in range(len(new_dic)):
    cnt += new_dic[i][1]
    if cnt >= k:
        break
    result += 1

print(result)