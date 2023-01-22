import sys
from collections import deque
input = sys.stdin.readline

queue = deque()

N = int(input())

def push_front(X):
    queue.appendleft(X)

def push_back(X):
    queue.append(X)

def pop_front():
    if (len(queue) != 0):
        print(queue.popleft())
    else:
        print("-1")

def pop_back():
    if (len(queue) != 0):
        print(queue.pop())
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


for i in range(N):
    line = list(map(str, input().split()))
    if (line[0] == "push_front"):
        push_front(int(line[1]))
    elif (line[0] == "push_back"):
        push_back(int(line[1]))
    elif (line[0] == "pop_front"):
        pop_front()
    elif (line[0] == "pop_back"):
        pop_back()
    elif (line[0] == "size"):
        size()
    elif (line[0] == "front"):
        front()
    elif (line[0] == "empty"):
        empty()
    else:
        back()
