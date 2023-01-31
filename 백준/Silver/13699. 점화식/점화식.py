n = int(input())
dp = [0] * 36
dp[0] = 1

if n == 0:
    print("1")
else:
    for i in range(1, 36):
        num = 0
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
    print(dp[n])





