def sol(n):
    if (n == 1 or n == 2):
        return 1 if n == 1 else 3
    dp = [0]*(n+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, n+1):
        dp[i] = dp[i-1]+2*dp[i-2]

    return dp[-1] % 10007


n = int(input())
print(sol(n))
