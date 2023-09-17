def binary(n):
    cnt = 0
    while (n != 0):
        n &= (n-1)
        cnt += 1
    return cnt


def solution(n):
    if (n == 1):
        return 0
    answer = 0
    m = binary(n)
    print(m)
    start = 0
    for i in range(m):
        start += 2**i
    for i in range(start, n):
        if (binary(i) == m):
            answer += 1

    return answer


print(solution(11))
