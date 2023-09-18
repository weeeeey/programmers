def solution(a, b):
    MOD = int(1e5)
    a %= MOD
    b %= MOD
    c = {}
    result = a
    k = 0
    for i in range(1, b):
        result = (result*a) % MOD
        if (result != a):
            c[i] = result
        else:
            k = i
            break
    if (k != 0):
        cc = b % k
        return c[cc-1]
    return c[cc]

    # return result


print(solution(123456789, 12345))
