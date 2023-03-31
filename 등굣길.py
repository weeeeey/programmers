from collections import deque

dx = [0,1]
dy = [1,0]
def solution(m, n, puddles): # m은 가로, n이 세로
    visited =[ [0]*(m+1) for i in range(n+1)]
    for ip in puddles:
        a,b=ip
        visited[b][a]=-1
    q = deque()
    q.append([1,1])    
    visited[1][1]=1
    while(q):
        x,y = q.popleft()
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if(nx>n or ny>m):
                continue
            if(visited[nx][ny]==-1):
                continue
            if(visited[nx][ny]==0):
                visited[nx][ny]=visited[x][y]
                q.append([nx,ny])
            else:
                visited[nx][ny]+=visited[x][y]
                
    return visited[n][m]%(int(1e9)+7)

    
print(solution(4,3,[[2,2]]))
