T = int(input())
dp = [[0] * 14 for _ in range(15)]
for i in range(1, 15):
    dp[0][i - 1] = i

for i in range(1, 15):
    for j in range(14):
        dp[i][j] = sum(dp[i - 1][:j + 1])

for i in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n - 1])