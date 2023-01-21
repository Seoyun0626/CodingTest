def func(k):
    global check
    check = 1
    if (k == M):
        for i in range(0, M):
            for j in range(i + 1, M):
                if (arr[i] > arr[j]):
                    check = 0
                    break
        if(check):
            print(*arr)
        
    else:
        for i in range(1, N + 1):
            if (not isused[i]):
                arr[k] = i
                isused[i] = 1
                func(k + 1)
                isused[i] = 0

N, M = list(map(int, input().split()))
arr = [0] * M
isused = [0] * (N + 1)
func(0)