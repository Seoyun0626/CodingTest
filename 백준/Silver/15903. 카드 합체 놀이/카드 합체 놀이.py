import heapq
import sys

input = sys.stdin.readline
heap = []

n, m = map(int, input().split())
tmp = list(map(int, input().split()))

for x in tmp:
    heapq.heappush(heap, x)

for _ in range(m):
    num1 = heapq.heappop(heap)
    num2 = heapq.heappop(heap)
    final_num = num1 + num2
    heapq.heappush(heap, final_num)
    heapq.heappush(heap, final_num)
print(sum(heap))


