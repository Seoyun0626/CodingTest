s = "{{123}}"
result = []
tmp = []
dic = {}
cnt_tmp = []

# s = s.lstrip("{{")
# s = s.rstrip("}}")
# print(s)
s = s.replace("{", "")
s = s.replace("}", "")
# print(s)
tmp = list(map(int, s.split(",")))

# print(tmp)
cnt_tmp = set(tmp)
# print(cnt_tmp)
for x in cnt_tmp:
    dic[x] = 0
for x in tmp:
    dic[x] += 1

dic = sorted(dic.items(), key = lambda x : x[1], reverse = True)
# print(dic)
for i in range(len(dic)):
    result.append(int(dic[i][0]))
print(result)