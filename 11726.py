
def sol(n):
    if (n < 4):
        return n
    INF = 10007
    a = 2
    b = 3
    c = 0
    for i in range(4, n+1):
        c = a+b
        a = b
        b = c
    return c % INF


N = int(input())
print(sol(N))
