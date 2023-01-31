n = int(input())
# N의 범위에 의해 크기 생성 index = 무게, dp[index] = 가져가야하는 최소 봉지 개수
# 경우의 수
# 1. 3kg전 5kg전 했을 때 모두 최소값이 존재 -> 둘 중 작은 값 +1
# 2. 3kg전 5kg전 했을 때 둘 중 하나에 최소값이 존재 -> 존재하는 것 +1
# 3. 3kg전 5kg전 했을 때 모두 최솟갑시 존재X -> 할당하지않음


dp = [-1] * 5001
dp[3] = 1
dp[5] = 1

if n <= 5:
    print(dp[n])
else:
    for i in range(6, n + 1):
        a, b = dp[i], dp[i]

        if dp[i - 5] != -1:
            a = dp[i - 5]
        if dp[i - 3] != -1:
            b = dp[i -3]

        if a > 0 and b > 0:
            dp[i] = min(a + 1, b + 1)
        elif a > 0 and b < 0:
            dp[i] = a + 1
        elif a < 0 and b > 0:
            dp[i] = b + 1
        else:
            dp[i] = -1
    print(dp[n])
