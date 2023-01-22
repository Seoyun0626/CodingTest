# DP: 전에 했던거를 CHOICE 할 때
# DP에서 중효한 것 -> 점화식
# test case: 할 때 마다 DP를 하면 런타임 오류 -> DP TABLE 모두 작성 후 선택 -> 숫자들의 범위가 작음


num = [[0] * 14 for _ in range(15)]

for i in range(0, 14):
    num[0][i] = i + 1

for i in range(1, 15):
    for j in range(14):
        num[i][j] = sum(num[i - 1][:j + 1])

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    print(num[k][n - 1])
