from copy import deepcopy


def solution(sequence):
    answer = 0
    n = len(sequence)
    k = 1
    for i in range(n):
        sequence[i] *= k
        k *= -1
    dp = [[0, 0] for i in range(n)]
    dp[0] = [sequence[0], sequence[0]]

    min_val = 100_000_000
    max_val = -100_000_000
    for i in range(1, n):
        dp[i][0] = min(sequence[i], sequence[i]+dp[i-1][0])
        dp[i][1] = max(sequence[i], sequence[i]+dp[i-1][1])

    min_val = min(map(min, dp))
    max_val = max(map(max, dp))

    return max(abs(min_val), abs(max_val))


print(solution([2, 3, -6, 1, 3, -1, 2, 4]))
