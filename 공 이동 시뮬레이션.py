from collections import deque

def solution(n, m, ex, ey, quer):
    answer = 0
    d = [[0,1],[0,-1],[1,0],[-1,0]]
    
    qLen = -1*(len(quer)+1)
    visited = [[False]*m for i in range(n)]
    q = deque()
    q.append((0,ex,ey))

    
    return answer


print(solution(2,5,0,1,[[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]	))