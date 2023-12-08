global value1, value2

def sol(N):
    dp = [0, 0, 1, 1]
    for i in range(4, N + 1):
        value1=1000000+1
        value2=1000000+1
        if (i % 2 == 0):
            value1 = dp[i//2] + 1
        if (i % 3 == 0):
            value2 = dp[i//3] + 1
        value3 = dp[i-1] + 1
        dp.append(min(value1, value2, value3))
    print(dp[N])
N = int(input())
sol(N)

