N = input()
cnt = 0
NEW_N = ""
flag = 0

while N != NEW_N:
    if flag == 0:
        if len(N) == 1:
            N = "0" + N
            total = str(int(N[0]) + int(N[1]))
            NEW_N = N[-1] + total[-1]
            flag = 1
        else:
            total = str(int(N[0]) + int(N[1]))
            NEW_N = N[-1] + total[-1]
            flag = 1
    else:
        if len(NEW_N) == 1:
            NEW_N = "0" + N
            total = str(int(NEW_N[0]) + int(NEW_N[1]))
            NEW_N = NEW_N[-1] + total[-1]
        else:
            total = str(int(NEW_N[0]) + int(NEW_N[1]))
            NEW_N = NEW_N[-1] + total[-1]
    cnt += 1
print(cnt)

