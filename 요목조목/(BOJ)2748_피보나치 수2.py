n = int(input())
#시간 초과 발생X
dp = [0] * 91
dp[0] = 0
dp[1] = 1
for i in range(2, 91):
    dp[i] = dp[i - 1] + dp[i - 2]
print(dp[n])


#시간 초과 발생O
def fibo(x):
    if x == 0:
        return 0
    if x == 1:
        return 1
    return fibo(x - 1) + fibo(x - 2)
print(fibo(n))