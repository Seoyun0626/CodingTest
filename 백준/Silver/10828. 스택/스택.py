#시간초과 - 파이썬 입력 받기
#여러줄을 입력 받을 때 input()으로 받는다면 시간 초과(import sys사용하기)

import sys

N = int(input())

def push(X):
    stack.append(int(X))

def pop():
    if(empty() == 0):
        num = stack.pop() #받아주는 값 있어야함
        print(num)
    else:
        print("-1")

def size():
    print(len(stack))

def empty():
    if(len(stack) != 0):
        return 0
    else:
        return 1

def top():
    if(empty() == 0):
        print(stack[-1])
    else:
        print("-1")

stack = []
for i in range(N):
    line = list(map(str, sys.stdin.readline().split()))
    if (line[0] == "push"):
        push(line[1])
    elif (line[0] == "top"):
        top()
    elif (line[0] == "size"):
        size()
    elif (line[0] == "pop"):
        pop()
    elif (line[0] == "empty"):
        print(empty())