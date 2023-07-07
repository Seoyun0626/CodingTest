import sys
input = sys.stdin.readline

n = int(input())
opinion = []
total = 0

for _ in range(n):
    score = int(input())
    opinion.append(score)
# print(opinion)

if n == 0:
    print(0)
else:
    opinion.sort()
    index = int((n * 0.15) + 0.5)
    for i in range(index, n-index):
        total += opinion[i]
    # print(total)
    print(int((total / (n - 2 * index)) + 0.5))
