import sys
input = sys.stdin.readline

queue = []
N = int(input())

while True:
    num = int(input())
    if num == -1:
        break
    else:
        if num > 0 and len(queue) < N:
            queue.append(num)
        elif num == 0:
            queue.pop(0)

if len(queue) == 0:
    print("empty")
else:
    print(*queue)