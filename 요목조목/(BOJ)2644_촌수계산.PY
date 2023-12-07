import sys
input = sys.stdin.readline

n = int(input())
num1, num2 = map(int, input().split())
m = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    p, c = map(int, input().split())


