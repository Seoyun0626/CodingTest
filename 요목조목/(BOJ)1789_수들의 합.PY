# 개수가 최대가 되기 위해서 -> 무조겅 1부터 더해야함

import sys

input = sys.stdin.readline

s = int(input())
n = 0
total = 0

while True:
    n += 1
    total += n
    if total > s:
        break
print(n - 1)
