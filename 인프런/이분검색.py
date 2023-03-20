import sys
# sys.stdin = open("input.txt","rt")
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
# print(arr)
start = 0
final = len(arr)
mid = (start + final) // 2

while M != arr[mid]:
    if M < arr[mid]:
        final = mid
        mid = (start + final) // 2
    else:
        start = mid
        mid = (start + final) // 2
print(mid+1)