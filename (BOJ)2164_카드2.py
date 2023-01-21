import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue = deque()
for i in range(1, N + 1):
    queue.append(i)
for i in range(1, N, 1):
    queue.popleft()
    queue.append(queue[0])
    queue.popleft()
print(*queue)

