nums = list(map(int, input().split()))
if nums[0]==nums[1]==nums[2]:
    print(nums[0])
else:
    tmp1=max(nums)
    tmp2=min(nums)
    index1=nums.index(tmp1)
    index2=nums.index(tmp2)
    index=3-index1-index2
    print(nums[index])