from collections import deque

dx = [0,1]
dy = [1,0]
INF = int(1e5)
def solution(m, n, puddles): # m은 가로, n이 세로
    answer = 0
    visited =[ [INF]*(m+1) for i in range(n+1)]
    for ip in puddles:
        a,b=ip
        visited[b][a]=-1
    q=deque()
    q.append((1,1))
    visited[1][1]=0
    while(q):
        x,y = q.popleft()
        for i in range(2):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx>n or ny>m):
                continue
            if(visited[nx][ny]==-1):
                continue
            if(visited[nx][ny]<visited[x][y]+1):
                continue
            if(nx==n and ny==m):
                answer+=1
                visited[nx][ny]=visited[x][y]+1
                continue
            visited[nx][ny]=visited[x][y]+1
            q.appendleft((nx,ny))
    return answer

print(solution(4,3,[[2,2]]))
