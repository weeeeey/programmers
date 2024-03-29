from collections import deque

dir = [
        [-1,0,-1,0],
        [1,0,1,0],
        [0,-1,0,-1],
        [0,1,0,1],
        ]


rot = [[[0,0,-1,-1,0,0,-1,0],[0,0,1,-1,0,0,1,0],[-1,1,0,0,-1,0,0,0],[1,1,0,0,1,0,0,0]],  [[0,0,-1,-1,0,0,0,-1],[0,0,-1,1,0,0,0,1],[1,-1,0,0,0,-1,0,0],[1,1,0,0,0,1,0,0]]]

def solution(gr):
    n = len(gr)
    visited = {}
    visited[0,0,0,1] = 0
    q= deque()
    q.append((0,0,0,1,0,0))
    answer = int(1e9)
    while(q):
        sx,sy,ex,ey,dic,d = q.popleft() # dic => 0 가로, 1 세로
        if [sx,sy]==[n-1,n-1] or [ex,ey]==[n-1,n-1]:
            answer = min(d,answer)
            continue
        for i in range(8):
            if i<4:
                nsx,nsy,nex,ney = sx+dir[i][0],sy+dir[i][1],ex+dir[i][2],ey+dir[i][3]
                if nsx<0 or nsy<0 or nex<0 or ney<0 or nsx>=n or nex>=n or nsy>=n or ney>=n:
                    continue
                if gr[nsx][nsy]==1 or gr[nex][ney]==1:
                    continue
                if (nsx,nsy,nex,ney) not in visited or visited[nsx,nsy,nex,ney]>d+1:
                    visited[nsx,nsy,nex,ney] = d+1
                    q.append((nsx,nsy,nex,ney,dic,d+1))
                    
            else:
                j=i-4
                nsx,nsy,nex,ney = sx+rot[dic][j][0],sy+rot[dic][j][1],ex+rot[dic][j][2],ey+rot[dic][j][3]
                csx,csy,cex,cey = sx+rot[dic][j][4],sy+rot[dic][j][5],ex+rot[dic][j][6],ey+rot[dic][j][7]
                if nsx<0 or nsy<0 or nex<0 or ney<0 or nsx>=n or nex>=n or nsy>=n or ney>=n:
                    continue
                if gr[nsx][nsy]==1 or gr[nex][ney]==1 or gr[csx][csy]==1 or gr[cex][cey]==1:
                    continue
                ddd = 1 if dic==0 else 0
                if j in [0,3]:
                    if ((nex,ney,nsx,nsy) not in visited or visited[nex,ney,nsx,nsy]>d+1) :
                        visited[nex,ney,nsx,nsy] = d +1    
                        q.append((nex,ney,nsx,nsy,ddd,d+1))
                else:
                    if ((nsx,nsy,nex,ney) not in visited or visited[nsx,nsy,nex,ney]>d+1):
                        visited[nsx,nsy,nex,ney] = d +1    
                        q.append((nsx,nsy,nex,ney,ddd,d+1))        

                        
    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))



