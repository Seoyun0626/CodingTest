import sys
from collections import deque
input = sys.stdin.readline

def push(X):
    queue.append(X)

def empty():
    if (len(queue) == 0):
        print("1")
    else:
        print("0")
def pop():
    if (len(queue) != 0):
        print(queue.popleft())
    else:
        print("-1")

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
def size():
    print(len(queue))

N = int(input())
queue = deque()
for i in range(N):
    line = list(map(str, input().split()))
    if (line[0] == "push"):
        push(int(line[1]))
    elif (line[0] == "front"):
        front()
    elif (line[0] == "back"):
        back()
    elif (line[0] == "size"):
        print(len(queue))
    elif (line[0] == "pop"):
        pop()
    else:
        empty()

