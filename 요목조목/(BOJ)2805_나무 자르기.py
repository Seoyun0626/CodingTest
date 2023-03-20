n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = 0
# print(arr)

start = 0
end = arr[-1]

def length(len):
    tree = 0
    for x in arr:
        if x > len:
            tree += (x - len)
    return tree

while start <= end:
    mid = (start + end) // 2
    if length(mid) >= m:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
    # print(start, end, res)
print(res)

