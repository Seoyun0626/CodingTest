import sys
input = sys.stdin.readline


price = []
cnt = 0
N, K = map(int, input().split())


for _ in range(N):
    price.append(int(input()))


price = price[::-1]


for x in price:
    if (K // x) != 0:
        cnt += K // x
        K = K - (K // x) * x

print(cnt)


