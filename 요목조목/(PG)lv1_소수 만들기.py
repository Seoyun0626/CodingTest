#for문 3바뀌 돌리기

from itertools import combinations

nums = [1,2,3,4]
def prime(x):
    cnt = 0
    for i in range(1, x + 1):
        if x % i == 0:
            cnt += 1
    if cnt == 2:
        return True

num_arr = list(map(sum, list(combinations(nums, 3))))
total = 0
for x in num_arr:
    if prime(x):
        total += 1
print(total)


