def solution(n):
    # 맨 마지막을 1칸 or 2칸으로 고정
    # n = 3 -> (n = 2 + 1칸 / n = 1 + 2칸)
    # n = k -> (n = k-1 + 1칸 / n = k-2 + 2칸)
    dp = [0] * (n+1)
    dp[0], dp[1] = 1, 1
    if n == 1:
        return 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    answer = dp[i] % 1234567
    return answer