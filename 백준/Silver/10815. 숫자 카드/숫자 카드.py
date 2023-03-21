n = int(input())
num = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))
num.sort()
# print(num)
result = []
def find(check_num):
    left = 0
    right = len(num)
    while left <= right:
        mid = (left + right) // 2
        if mid >= len(num):
            return 0
        if check_num == num[mid]:
            return 1
        elif check_num < num[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return 0



for x in check:
    if find(x) == 1:
        result.append(1)
    else:
        result.append(0)
print(*result)



