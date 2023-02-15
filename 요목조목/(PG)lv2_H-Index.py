# citations = [6, 6, 6, 6, 6, 1]
# citations = [3, 0, 6, 1, 5]
# citations = [10, 8, 5, 4, 3]
h = len(citations)
citations.sort(reverse = True)
print(citations)
dic = {}
for x in citations:
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] += 1
print(dic)

while h > 0:
    cnt = 0
    for key, value in dic.items():
        if key >= h:
            cnt += value
    # print(cnt, h)
    if cnt >= h:
        break
    else:
        h -= 1
print(h)



