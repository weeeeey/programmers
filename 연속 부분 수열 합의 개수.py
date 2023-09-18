def solution(elements):
    answer = 0
    n = len(elements)
    arr = elements+elements
    dp = [[0]*(2*n) for i in range(n+1)]
    result = []
    for i in range(1, n+1):
        for j in range(n):
            dp[i][j] = dp[i-1][j]+arr[j+i-1]
            result.append(dp[i][j])

    return len(set(result))


# 3<=길이<=1_000

print(solution([7, 9, 1, 1, 4]))
