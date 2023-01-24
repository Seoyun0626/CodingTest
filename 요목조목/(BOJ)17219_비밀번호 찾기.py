import sys
input = sys.stdin.readline


N, M = map(int, input().split())
info = {}


for _ in range(N):
    key, value = map(str, input().split())
    info[key] = value


for _ in range(M):
    site = input().rstrip()
    print(info[site])
