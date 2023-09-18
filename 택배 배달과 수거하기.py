def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries.reverse()
    pickups.reverse()
    d_val = 0
    p_val = 0
    for i in range(n):
        d_val += deliveries[i]
        p_val += pickups[i]
        while (d_val > 0 or p_val > 0):
            d_val -= cap
            p_val -= cap
            answer += (n-i)*2

    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))
