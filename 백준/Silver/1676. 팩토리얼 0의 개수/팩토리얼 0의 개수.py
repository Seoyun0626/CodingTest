import sys
input = sys.stdin.readline


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

N = int(input())


num = factorial(N)
num = list(str(num))
cnt = 0
num = num[::-1]


for i in range(len(num)):
    if num[i] != "0":
        print(cnt)
        break
    else:
        cnt += 1

