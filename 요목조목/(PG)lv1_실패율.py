# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
# N = 4
# stages = [4, 4, 4, 4, 4]
dict = {}
result = []
length = len(stages)
i = 1
while i <= N:
    cnt = 0
    for j in range(len(stages)):
        if stages[j] == i:
            cnt += 1
    if length == 0:
        dict[i] = 0
    else:
        dict[i] = cnt / length
        length = length - cnt
    i += 1


new_dict = sorted(dict.items(), key = lambda x : x[1], reverse = True)


for i in range(len(new_dict)):
    result.append(new_dict[i][0])
print(result)

