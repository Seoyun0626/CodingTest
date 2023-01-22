N, M = map(int, input().split())
total = []
check = []

for _ in range(N):
    total.append(input())

for i in range(N - 7):
    for j in range(M - 7): # 여기에서 사용된 for문은 total을 벗어나지 않기 위해
        index1 = 0 #시작점이 흰색일 때
        index2 = 0 #시작점이 검정색일 때
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0: #시작점과 같은 색이어야함
                    if total[a][b] == "B": #만약에 W로 시작점 그러면 계속 W
                        index1 += 1
                    else:
                        index2 += 1
                else: #시작점과 반대색이어야함
                    if total[a][b] == "B": #만약에 B로 시작점 그러면 여기는 시작점과 반대인 W색
                        index2 += 1
                    else:
                        index1 += 1
        check.append(min(index1, index2))
print(min(check))