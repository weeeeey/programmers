def solution(n):
    answer = 0
    if (n % 3 != 0):
        return 0
    dp = [0]*(n+1)
    dp[1] = 2
    dp[2] = 2
    dp[3] = 3
    for i in range(4, n+1):
        if (i % 3 == 1):
            dp[i] = dp[i-1]*2 + dp[i-3]
        else:
            dp[i] = dp[i-1]+dp[i-3]

    return dp[n] % 1000000007


T = int(input())
for i in range(T):
    N = int(input())
    print(solution(N))
