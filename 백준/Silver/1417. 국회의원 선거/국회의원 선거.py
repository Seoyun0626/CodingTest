import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []
cnt = int(input())
result = 0


for _ in range(N - 1):
    heapq.heappush(heap, -int(input()))
# print(cnt, heap)

while True:
    if len(heap) == 0:
        break
    check = -heapq.heappop(heap)
    if check < cnt:
        break
    else:
        check -= 1
        cnt += 1
        result += 1
        heapq.heappush(heap, -check)
print(result)


