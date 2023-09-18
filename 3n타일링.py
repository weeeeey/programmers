def solution(n):
    if (n % 2 != 0):
        return 0
    answer = 0
    INF = 1_000_000_007
    dp = [0]*(n+1)
    dp[1] = 2
    dp[2] = 3
    for i in range(3, n+1):
        if (i % 2 == 1):
            dp[i] = (dp[i-1]*2 + dp[i-2]) % INF
        else:
            dp[i] = (dp[i-1]+dp[i-2]) % INF

    return dp[n]


print(solution(4))
