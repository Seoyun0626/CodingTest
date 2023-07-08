import sys
from itertools import combinations_with_replacement

n, m = map(int, input().split())
num = []
result = []

for i in range(1, n + 1):
    num.append(i)
# print(num)

for tmp in combinations_with_replacement(num, m):
    print(*tmp)
