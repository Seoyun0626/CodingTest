n = int(input())
arr = list(range(1, n + 1, 1))
# print(arr)
cnt = 0
for x in arr:
    if x // 10 == 0:
        cnt += 1
    elif x // 100 == 0:
        cnt += 1
    elif x // 1000 == 0:
        x = str(x)
        if int(x[2]) - int(x[1]) == int(x[1]) - int(x[0]):
            cnt += 1
print(cnt)


