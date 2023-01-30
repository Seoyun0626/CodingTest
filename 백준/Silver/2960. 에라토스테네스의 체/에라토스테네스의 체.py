N, K = map(int, input().split())
arr = [True] * (N + 1)
result = []
for i in range(2, N + 1):
    if arr[i] == True:
        arr[i] = False
        result.append(i)
    j = 2
    while i * j <= N:
        if arr[i * j] == True:
            arr[i * j] = False
            result.append(i * j)
        j += 1
print(result[K - 1])
