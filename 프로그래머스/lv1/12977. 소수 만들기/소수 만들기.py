def solution(nums):
    from itertools import combinations
    def prime(x):
        cnt = 0
        for i in range(1, x + 1):
            if x % i == 0:
                cnt += 1
        if cnt == 2:
            return True


    num_arr = list(map(sum,list(combinations(nums,3))))
    total = 0
    for x in num_arr:
        if prime(x):
            total+= 1


    return total