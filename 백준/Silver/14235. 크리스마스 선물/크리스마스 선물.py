import heapq

n = int(input())
arr = []


for i in range(n):
    check = input()
    # print(check, arr)
    if len(check) == 1:
        if len(arr) == 0:
            print("-1")
        else:
            print(-1 * heapq.heappop(arr))
    else:
        tmp = list(map(int, check.split()))
        for i in range(1, len(tmp)):
            heapq.heappush(arr, -1 * tmp[i])

