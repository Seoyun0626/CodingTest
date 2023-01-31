def solution(nums):
    cnt = 1
    result = []
    result.append(nums[0])
    if len(nums) == 2:
        return cnt
    for i in range(1, len(nums)):
        tmp = nums[i]
        if tmp not in result:
            result.append(tmp)
            cnt += 1
            if cnt == (len(nums) // 2):
                return cnt
    return cnt