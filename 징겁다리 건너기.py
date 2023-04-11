from collections import deque
INF = 2*int(1e9)

def solution(stones, k):
    answer = INF
    n = len(stones)
    if(n==k):
        return max(stones)
    dp = [[INF]*n for i in range(k)]
    q = deque()
    for i in range(k):
        q.a

    # for i in [0,k]:
    #     while(True):
    #         num = max(stones[i:i+k])
    #         if(n-i<=k):
    #             answer = min(min(dp),answer)
    #             break
    #         else:
    #             dp[i:i+k]=[num]*(k)
    #             i+=k
    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))

# k개로 묶여진 묶음을 찾고 그 묶음 중의 최댓값이 가장 작은 값을 찾기 

# k번째로 작은 수를 찾기? => 실패
