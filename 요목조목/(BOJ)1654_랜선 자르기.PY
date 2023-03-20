# zerodivisionerror : mid 값은 1이상이야함

k, n = map(int, input().split())
arr = []

for _ in range(k):
    arr.append(int(input()))
arr.sort()
# print(arr)

def Count(len):
    cnt = 0
    for x in arr:
        cnt += (x // len)
    return cnt


start = 1
end = arr[-1]

while start <= end:
    mid = (start + end) // 2
    if Count(mid) >= n:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)

