import sys
input = sys.stdin.readline

N = int(input())
result = []
time = list(map(int, input().split()))
time.sort()

for i in range(N):
    result.append(sum(time[:i +1]))
print(sum(result))

