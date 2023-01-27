import sys
input = sys.stdin.readline


N = int(input())
dic = {}


for _ in range(N):
    participant = input().rstrip()
    if participant in dic:
        dic[participant] += 1
    else:
        dic[participant] = 1
for _ in range(N - 1):
    final = input().rstrip()
    dic[final] -= 1
for p in dic:
    if dic[p]:
        print(p)
        break



