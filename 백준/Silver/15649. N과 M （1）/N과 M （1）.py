def func(k): #arr의 k번째 수를 택하는 함수
    if (k == M):
        print(*arr)
    else:
        for i in range(1, N + 1):
            if (not isused[i]):
                arr[k] = i
                isused[i] = 1
                func(k + 1)
                isused[i] = 0

N, M = list(map(int, input().split()))
arr = [0] * (M)
isused = [0] * (N + 1)
func(0)