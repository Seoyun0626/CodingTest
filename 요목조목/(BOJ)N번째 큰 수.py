# 메모리 초과 -> 숫자 모두를 배열에 저장 후 조건에 따라 처리불가
# 입력받을 때 마다 heap의 최솟값과 입력받은 배렬의 크기 비교 -> 최종적으로 큰 값들 만 N개 생성
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










