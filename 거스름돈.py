INF = int(1e9)+7

def solution(n, money):
    answer = 0
    m = len(money)
    dp = [[0]*(n+1) for i in range(m)]
    dp[0][0]=1
    for j in range(1,(n//money[0])+1):
        dp[0][j*money[0]]=1
                
    for i in range(1,m):
        for j in range(n+1):
            if j<money[i]:
                dp[i][j]=dp[i-1][j]
                continue
            dp[i][j]= dp[i-1][j]+dp[i][j-money[i]]
    
    for i in range(m):
        print(dp[i])
    

    answer=dp[m-1][n]
    
    return answer%INF

print(solution(5,[1,2,5]))
