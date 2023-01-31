N = int(input())
cnt = 0
flag = 0
while N >= 0:
    if N % 5 == 0:
        cnt += N // 5
        print(cnt)
        flag = 1
        break
    N -= 3
    cnt += 1
if flag == 0:
    print("-1")