from collections import deque

N = int(input())
result = []
queue = deque()
for i in range(1, N + 1):
    queue.append(i)

while queue:
    result.append(queue.popleft())
    if len(queue) != 0:
        num = queue.popleft()
        queue.append(num)
print(*result)
