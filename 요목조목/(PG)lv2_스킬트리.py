skill = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
cnt = 0
skill_tmp = []
for x in skill_trees:
    tmp = ""
    for i in range(len(x)):
        if x[i] in skill:
            tmp += x[i]
    skill_tmp.append(tmp)
# print(skill_tmp)

for x in skill_tmp:
    flag = 0
    for i in range(len(x)):
        if x[i] != skill[i]:
            flag =1
            break
    if flag == 0:
        # print(x)
        cnt += 1
print(cnt)
