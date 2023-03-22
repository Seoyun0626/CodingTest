import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
money = int(input())
# print(arr)
res = 0

def sum_money(tmp):
    total = 0
    for x in arr:
        if tmp - x > 0:
            total += x
        else:
            total += tmp
    return total


start = 0
end = arr[-1]
while start <= end:
    mid = (start + end) // 2
    if sum_money(mid) <= money:
        res = mid
        start = mid + 1
    else:
        end = mid - 1
print(res)