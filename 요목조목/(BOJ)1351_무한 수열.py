# 시간초과 방지할려면 dict가 짱이다
# do 의 top - down 방식을 사용하자 => 아직 미해결

import sys

sum_dict = {}
sum_dict[0] = 1
input = sys.stdin.readline

n, p, q = map(int, input().split())

for i in range(1, n + 1):
    sum_dict[i] = sum_dict[i // p] + sum_dict[i // q]

print(sum_dict[n])
