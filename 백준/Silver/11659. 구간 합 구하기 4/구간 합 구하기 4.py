#누적 합(DP의 개념과 비슷) -> 리스트 추가 구현 + 계산된 값 미리 넣기

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))
result = [0]
tmp = 0
for i in num:
    tmp += i
    result.append(tmp)

for j in range(M):
    a, b= map(int, input().split())
    print(result[b] - result[a - 1])

