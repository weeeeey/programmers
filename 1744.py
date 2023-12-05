
MIN_INF = -int(1e9)

N = int(input().rstrip())
ARR = []
for _ in range(N):
    ARR.append(int(input().rstrip()))
ARR.sort(reverse=True)


def solution(n, arr):
    if (n == 1):
        return arr[0]
    dp = [MIN_INF]*n
    dp[0] = arr[0]
    dp[1] = max(arr[0]+arr[1], arr[0]*arr[1])

    for i in range(2, n):
        dp[i] = max(dp[i-1]+arr[i], dp[i-2]+arr[i-1]*arr[i])
    return dp[n-1]


print(solution(N, ARR))
