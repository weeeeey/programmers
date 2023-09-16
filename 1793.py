def countWaysToFillRectangle(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + 2*dp[i - 2]

    return dp[n]


# 여러 개의 테스트 케이스를 처리
while True:
    try:
        n = int(input())
        ways = countWaysToFillRectangle(n)
        print(ways)
    except EOFError:
        break
