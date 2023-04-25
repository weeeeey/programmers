# 열쇠의 돌기(1)-> 자물쇠 홈(0) 0
# 자물쇠 영역 안에선 열쇠의 돌기(1) -> 자물쇠 돌기(1) x


from copy import deepcopy
from collections import deque

dx = [1,0] #아래, 오른쪽
dy = [0,1]

def solution(key, lo):
    m,n = len(key),len(lo) 
    result = 0
    for i in range(n): 
        result+=lo[i].count(0)
    temp = [[-1]*3*n for i in range(3*n)]
    for i in range(n):
        for j in range(n):
            temp[i+n][j+n]=lo[i][j]
    lock = deepcopy(temp)
    for rotation in range(4):   
        if rotation!=0:
            temp = [[0]*m for i in range(m)]
            for j in range(m):
                for i in range(m):
                    temp[i][j] = key[m-1-j][i]
            key=deepcopy(temp)
            
                
        visited = [[False]*3*n for i in range(3*n)]
        visited[0][0]=True
        q = deque()
        q.append((0,0,m,m,0,0))
        while(q):
            sx,sy,ex,ey,x,y= q.popleft()
            tri = False
            cnt = 0
            for i in range(sx,ex):
                for j in range(sy,ey):
                    if lock[i][j]==1 and key[i-x][j-y]==1:
                        tri= True
                        break
                    if lock[i][j]==0 and key[i-x][j-y]==1:
                        cnt+=1
                if tri==True:
                    break
            
            
            if tri==False and cnt==result:
                return True
            else:
                for k in range(2):
                    nsx = sx+dx[k]
                    nex = ex+dx[k]
                    nsy = sy+dy[k]
                    ney = ey+dy[k]
                    if nex>=3*n or ney>=3*n :
                        continue
                    if visited[nsx][nsy]==True:
                        continue
                    visited[nsx][nsy] = True
                    q.append((nsx,nsy,nex,ney,x+dx[k],y+dy[k]))
                        
    

    return False
