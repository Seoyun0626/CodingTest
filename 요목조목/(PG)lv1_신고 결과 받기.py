id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]
# k = 3
report = list(set(report))


mid_dic = {}
for x in id_list:
    mid_dic[x] = 0
final_dic = {}
for x in id_list:
    final_dic[x] = 0

bad_name = []
result = []

for i in range(len(report)):
    # print(report)
    good, bad = map(str, report[i].split())
    mid_dic[bad] += 1
print(mid_dic)

for name, num in mid_dic.items():
    print(name, num, k)
    if num >= k:
        bad_name.append(name)
print(bad_name)

for i in range(len(report)):
    good, bad = map(str, report[i].split())
    if bad in bad_name:
        final_dic[good] += 1

for num in final_dic.values():
    result.append(num)
print(result)