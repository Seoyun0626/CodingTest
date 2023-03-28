# cur 활용하기

n, c = map(int, input().split())
arr= []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
# print(arr)

lt = 1
rt = arr[-1] - arr[0]
# print(lt, rt)


def count(mid):
    cur = arr[0]
    cnt = 1
    for i in range(n):
        if arr[i] - cur >= mid:
            cnt += 1
            cur = arr[i]
    return cnt


while lt <= rt:
    mid = (lt + rt) // 2
    cnt = count(mid)
    # print(lt,rt,mid,cnt)
    if cnt >= c:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1
print(res)

