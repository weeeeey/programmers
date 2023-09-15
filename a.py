from copy import deepcopy


def solution(triangle):
    n = len(triangle)
    dp = [[0]*(n+1) for i in range(n)]
    dp[0][1] = triangle[0][0]
    for i in range(1, n):
        for j in range(1, i+2):
            dp[i][j] = triangle[i][j-1]+max(dp[i-1][j], dp[i-1][j-1])

    return max(dp[-1])


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
