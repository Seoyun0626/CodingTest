import sys
input = sys.stdin.readline
 
n = int(input())
total_plug = 0
 
for _ in range(n):
    plug = int(input())
    total_plug += plug
 
print(total_plug-(n-1))