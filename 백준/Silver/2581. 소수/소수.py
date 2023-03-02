import sys

input = sys.stdin.readline

M = int(input())
N = int(input())
result = []
if M != 1 or N != 1:
    for i in range(M, N + 1):
        num = i
        cnt = 0
        for j in range(1, num + 1):
            if num % j == 0:
                cnt += 1
        if cnt == 2:
            result.append(num)
        # print(num, cnt, result)
if len(result) == 0:
    print("-1")
else:
    print(sum(result))
    print(min(result))

