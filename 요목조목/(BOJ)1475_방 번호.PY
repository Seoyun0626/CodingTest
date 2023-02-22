import math

room = input()
dic = {}


for i in range(10):
    dic[str(i)] = 0
# print(dic)

for x in room:
    dic[x] += 1
# print(dic)

if '9' in dic:
    dic['6'] += dic['9']
    del dic['9']

# print(dic)

if '6' in dic:
    dic['6'] = math.ceil(dic['6'] / 2)

# print(dic)

all_values = dic.values()
max_values = max(all_values)
print(max_values)