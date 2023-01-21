def func(k):
    if (k == M):
        print(*arr)
    else:
        for i in range(1, N + 1):
            arr[k] = i
            func(k + 1)



N, M = list(map(int, input().split()))
arr = [0] * M
isused = [0] * (N + 1)
func(0)