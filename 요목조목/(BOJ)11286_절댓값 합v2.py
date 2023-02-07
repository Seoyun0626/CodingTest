# 시간 초과
# 힙을 튜플로 구성 -> 튜플의 앞 숫자만을 이용하여 정렬

import heapq
import sys


input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(num), num))



