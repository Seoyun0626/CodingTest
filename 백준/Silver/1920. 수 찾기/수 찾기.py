import sys

N = int(sys.stdin.readline())
standard = list(map(int, sys.stdin.readline().split()))
standard.sort()
M = int(sys.stdin.readline())
compare = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    first = 0
    last = len(standard) - 1
    while first <= last:
        mid = (first + last) // 2
        if (standard[mid] == compare[i]):
            print("1")
            break
        if (standard[mid] > compare[i]):
            last = mid - 1
        else:
            first = mid + 1
    else:
        print("0")