import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

def first_command():
    queue.popleft()

def second_command():
    num = queue.popleft()
    queue.append(num)

def third_command():
    num = queue.pop()
    queue.appendleft(num)

N, M = map(int, input().split())
for i in range(1, N + 1, 1):
    queue.append(i)


arr = list(map(int, input().split()))
cnt = 0


for i in range(M):
    if (queue[0] == arr[i]):
        first_command()
    else:
        if (len(queue) / 2) > (queue.index(arr[i])):
            while(arr[i] != queue[0]):
                second_command()
                cnt += 1
                if (queue[0] == arr[i]):
                    first_command()
                    break
        else:
            while(arr[i] != queue[0]):
                third_command()
                cnt += 1
                if (queue[0] == arr[i]):
                    first_command()
                    break
print(cnt)










