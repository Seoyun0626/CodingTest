# 정렬 기준이 2가지
import sys
input = sys.stdin.readline

n = int(input())
info = []
for _ in range(n):
    start, end = map(int, input().split())
    info.append((start,end))
info = sorted(info, key=lambda x : (x[1],x[0]))
# print(info)

start, end = info[0][0], info[0][1]
cnt = 1
for i in range(1, len(info)):
    if info[i][0] >= end:
        cnt += 1
        end = info[i][1]
print(cnt)
