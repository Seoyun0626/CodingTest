import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

def push(X):
    queue.append(X)

def pop():
    if (len(queue) != 0):
        print(queue.popleft())
    else:
        print("-1")

def size():
    print(len(queue))

def empty():
    if (len(queue) != 0):
        print("0")
    else:
        print("1")

def front():
    if (len(queue) != 0):
        print(queue[0])
    else:
        print("-1")

def back():
    if (len(queue) != 0):
        print(queue[-1])
    else:
        print("-1")

N = int(input())
for i in range(N):
    line = list(map(str, input().split()))
    if (line[0] == "push"):
        push(int(line[1]))
    elif (line[0] == "front"):
        front()
    elif (line[0] == "back"):
        back()
    elif (line[0] == "size"):
        size()
    elif (line[0] == "empty"):
        empty()
    else:
        pop()