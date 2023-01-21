from collections import deque

N, K = map(int,input().split())
q = deque(list(range(1, N + 1)))

print("<", end="")
for i in range(N - 1):
    q.rotate(-(K - 1))
    print(q.popleft(), end=", ")
print(q[0], end=">")
