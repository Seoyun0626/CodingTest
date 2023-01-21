import sys

k = int(input())
stack = []

for i in range(k):
    num = sys.stdin.readline()
    num = int(num)
    if (num != 0):
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))



