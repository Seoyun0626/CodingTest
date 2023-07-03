# 최솟값, 최댓값을 빠르게 찾기 -> heap 사용
# 우선순위 큐
# 내 사견 : 뭔가 누적 합 같은 느낌 그래서 최소 누적합을 할 때 heap을 사용하면 되지 않을까??..

import heapq
import sys

heap = []
input = sys.stdin.readline
result = 0

N = int(input())
for _ in range(N):
    num = int(input())
    heapq.heappush(heap, num)
# print(heap)

if N == 1:
    print(0)
else:
    for i in range(N - 1):
        pre = heapq.heappop(heap)
        post = heapq.heappop(heap)
        result += pre + post
        heapq.heappush(heap, pre + post)
    print(result)



