def solution(triangle):
    answer = 0
    n = len(triangle)
    for i in range(n):
        triangle[i]=[0]+triangle[i]
    dp = [[0]*(n+1) for i in range(n)]
    for i in range(n):
        for j in range(1,i+2):
            dp[i][j]=triangle[i][j]
    for i in range(1,n):
        for j in range(1,i+2):
            dp[i][j] = dp[i][j] + max(dp[i-1][j],dp[i-1][j-1])

    return max(dp[n-1])

if __name__=='__main__':
    t=[]
    for i in range(5):
        t.append(list(map(int,input().rsplit()))) 
    print(solution(t))