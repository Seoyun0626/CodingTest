C = int(input())


for _ in range(C):
    cnt = 0
    arr = list(map(int, input().split()))
    arr = arr[1:]
    av = sum(arr) / len(arr)
    for x in arr:
        if x > av:
            cnt += 1
    result = round(cnt / len(arr) * 100 , 3)
    print(format(result, ".3f"), end="")
    print("%")