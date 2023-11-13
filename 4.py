def solution(n):
    l = 1
    c = 9
    while n > l * c:
        n -= l * c
        l += 1
        c *= 10

    s = 1 * 10 ** (l - 1)
    num = s + (n - 1) // l

    d = (n - 1) % l
    return str(num)[d]


print(solution(5))  # Example usage
