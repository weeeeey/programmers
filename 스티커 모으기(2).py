from collections import deque

dx = [2,3]
def solution(s):
    answer = 0
    n = len(s)
    if(n<=3):
        return max(s)
    dp = [[0]*n for i in range(2)]
    dp[0][0]=s[0]
    dp[1][1]=s[1]
    for j in range(2):
        for i in range(2,n):
            for k in range(2):
                num = i-dx[k]
                if(num<0):
                    continue
                dp[j][i]=max(dp[j][num]+s[i],dp[j][i])
    dp[0][-1]-=s[0]
    answer = max(max(dp[1]),max(dp[0]))
    return answer


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))