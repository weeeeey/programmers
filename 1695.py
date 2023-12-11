n = int(input().rstrip())
arr = list(map(int, input().rsplit()))
brr = arr[::-1]
dp = [[0]*n for _ in range(n)]
dp[0][0] = 0 if arr[0] != brr[0] else 1

for i in range(1, n):
    dp[0][i] = 1 if arr[i] == brr[0] else dp[0][i-1]

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = 1 if arr[j] == brr[i] else dp[i-1][j]
        else:
            if arr[j] == brr[i]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(n-dp[n-1][n-1])
