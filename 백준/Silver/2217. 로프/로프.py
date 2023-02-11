import sys
input = sys.stdin.readline


n = int(input())
nl = list() # num list
for _ in range(n):
    nl.append(int(input()))
nl.sort(reverse=True)
max_num = 0
for i in range(0, n):
    sum_tmp = nl[i] * (i + 1)
    if sum_tmp >= max_num:
        max_num = sum_tmp
 

print(max_num)
