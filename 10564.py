def sol(total_target,  arr):
    answer = 0
    dp = [[] for i in range(total_target+1)]
    for a in arr:
        dp[a].append(a)


T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    print(sol(n,  arr))
