# last = 0 : 마지막 값 저장
# 튜플값으로 list에 저장
# 문자열 res=""
# tmp = 비교 list
n = int(input())
arr = list(map(int, input().split()))
result = {}
flag = 0
left = arr[0]
right = arr[-1]

if left < right:
    result[left] = "L"
    arr.pop(0)
    left = arr[0]
else:
    result[right] = "R"
    arr.pop(-1)
    right = arr[-1]

while flag == 0:
    tmp = list(result.keys())[-1]
    # print(left,right,tmp)
    if left < right:
        if tmp < left:
            result[left] = "L"
            arr.pop(0)
            left = arr[0]
        elif tmp < right:
            result[right] = "R"
            arr.pop(-1)
            right = arr[-1]
        else:
            flag = 1
    else:
        if tmp < right:
            result[right] = "R"
            arr.pop(-1)
            right = arr[-1]
        elif tmp < left:
            result[left] = "L"
            arr.pop(0)
            left = arr[0]
        else:
            flag = 1
print(len(result))
total = list(result.values())
for x in total:
    print(x,end="")



