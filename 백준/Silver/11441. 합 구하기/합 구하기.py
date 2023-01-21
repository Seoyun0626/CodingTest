import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
M = int(input())

result = [0]
tmp = 0
for i in num:
    tmp += i
    result.append(tmp)

for j in range(M):
    a, b= map(int, input().split())
    print(result[b] - result[a - 1])