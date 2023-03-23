n = int(input())
res = 0
info = {}
for _ in range(n):
    height, weight = map(int, input().split())
    info[height] = weight
info = sorted(info.items(), key = lambda x : x[0], reverse= True)
# print(info,type(info))

for i in range(len(info)):
    flag = 0
    for j in range(0,i):
        if info[i][1] < info[j][1]:
            flag = 1
            break
    if flag == 0:
        # print(i,)
        res += 1
print(res)
