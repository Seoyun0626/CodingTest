# 1사분면을 2차원 배열(101 * 101)에 투영
# 맨 왼쪽 모서리를 기준으로 넓이 1로 측정 -> 길이10이 기준이 아니고 길이 9가 기준

n = int(input())
arr = []
paper = [[0] * 101 for _ in range(101)]
# print(paper)
for _ in range(n):
    index = list(map(int, input().split()))
    arr.append(index)
# print(arr)
total = 0
for x,y in arr:
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            # print(j,i)
            if paper[j][i] == 0:
                total += 1
                paper[j][i] = 1

print(total)
