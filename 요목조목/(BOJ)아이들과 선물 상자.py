import sys
import heapq

input = sys.stdin.readline
N, M = map(int, input().split())
present_cnt = list(map(int, input().split()))
children_cnt = list(map(int, input().split()))
heap = []
result = 1


for x in present_cnt:
    heapq.heappush(heap, -x)

for x in children_cnt:
    check = -heapq.heappop(heap)
    if check >= x:
        check -= x
        if check != 0:
            heapq.heappush(heap, -check)
    else:
        result = 0
        flag = 0
        break
print(result)

