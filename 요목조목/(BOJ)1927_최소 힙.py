import heapq
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input().rstrip())
    if x > 0:
        heapq.heappush(heap, x)
    else:
        if len(heap) == 0:
            print("0")
        else:
            print(heapq.heappop(heap))

