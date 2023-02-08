# 메모리 초과 -> 숫자 모두를 배열에 저장 후 조건에 따라 처리불가
# 입력받을 때 마다 최솟값 유무 확인해서 배열에 저장해주기
import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    if len(heap) != n:
        for x in tmp:
            heapq.heappush(heap, x)
    else:
        for x in tmp:
            mini = heapq.heappop(heap)
            if x > mini:
                heapq.heappush(heap, x)
            else:
                heapq.heappush(heap, mini)
    # print(heap)
print(heapq.heappop(heap))










