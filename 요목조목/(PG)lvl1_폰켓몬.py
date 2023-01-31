#같은 종류이면 같은 번호 -> 같은 번호이면 구분하기 어려움 => hash사용

nums = [3,1]
cnt = 1
result = []
flag = 0
result.append(nums[0])
if len(num) == 2:
    print(cnt)
    break
for i in range(1, len(nums)):
    tmp = nums[i]
    if tmp not in result:
        result.append(tmp)
        cnt += 1
        if cnt == (len(nums) // 2):
            flag = 1
            print(cnt)
            break
if flag == 0:
    print(cnt)

