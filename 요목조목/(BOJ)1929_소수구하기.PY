# N,M 사이의 소수 판별하기
#1제외하고 시작하기

import math

M, N = map(int, input().split())
def prime(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True

for i in range(M, N + 1):
    if prime(i):
        print(i)



