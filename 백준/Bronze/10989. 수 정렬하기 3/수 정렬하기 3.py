import sys


input = sys.stdin.readline

n = int(input())
cnts = [0] * 10001
for _ in range(n):
    cnts[int(input())] += 1

for i in range(1, 10001):
    while cnts[i]:
        print(i)
        cnts[i] -= 1