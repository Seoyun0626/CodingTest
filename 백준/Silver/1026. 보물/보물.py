import copy

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = 0
tmp = copy.deepcopy(B)
tmp.sort()

A.sort()
A = A[::-1]

for i in range(N):
    result += A[i] * tmp[i]
print(result)


