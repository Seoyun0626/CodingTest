import sys

a, b = map(int, sys.stdin.readline().split())
temp = []
for i in range(1, b + 1):
    for j in range(i):
        temp.append(i)

print(sum(temp[a - 1:b]))