n, m = map(int, input().split())
info = list(map(int, input().split()))
info.sort(reverse = True)
# print(info)

cnt = 0
while len(info) > 1:
    if info[0] + info[-1] > m:
        info.pop(0)
        cnt += 1
    else:
        info.pop(0)
        info.pop(-1)
        cnt += 1
if len(info) == 1:
    cnt += 1
else:
    cnt
print(cnt)




