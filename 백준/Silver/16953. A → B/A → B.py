A, B = map(int, input().split())
cnt = 0
while A < B:
    if B % 2 != 0 and B % 10 != 1:
        break
    if B % 2 == 0:
        B = B // 2
        cnt += 1
    elif B % 10 == 1:
        B = B // 10
        cnt += 1
    # print(B, cnt)
if A == B:
    print(cnt + 1)
else:
    print("-1")