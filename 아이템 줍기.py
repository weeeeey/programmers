from collections import deque


def solution(rec, chx, chy, ix, iy):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    INF = int(1e9)
    answer = INF
    gr=[[[] for j in range(51)] for i in range(51)]
    inner = [[[False]*len(rec) for i in range(51)]for j in range(51)]
    for i in range(len(rec)):
        ax,ay=rec[i][0],rec[i][1]
        cx,cy=rec[i][2],rec[i][3]
        for j in range(ay,cy+1):
            gr[ax][j].append(i)
            gr[cx][j].append(i)
        for j in range(ax+1,cx):
            gr[j][ay].append(i)
            gr[j][cy].append(i)
        for j in range(ax,cx+1):
            for k in range(ay,cy+1):
                inner[j][k][i]=True

    visited = [[INF]*51 for i in range(51)]
    visited[chx][chy]=0
    q = deque()
    if len(gr[chx][chy])==1:
        q.append((gr[chx][chy][0],chx,chy,-1,gr[chx][chy][0]))
    else:
        for cur in gr[chx][chy]:
            for a in gr[chx][chy]:
                if a!=cur:
                    other=a
            for i in range(4):
                ccx=chx+dx[i]
                ccy=chy+dy[i]
                if ccx<=0 or ccy<=0 or ccx>50 or ccy>50:
                    continue
                if gr[ccx][ccy]==[]:
                    continue
                if inner[ccx][ccy][other]==True:
                    continue

                if len(gr[ccx][ccy])==1 and gr[ccx][ccy][0]==cur:
                    q.append((cur,ccx,ccy,-1,cur))
                    visited[ccx][ccy]=1
                
                if len(gr[ccx][ccy])>=2:
                    for j in gr[ccx][ccy]:
                        if j==cur:
                            continue
                        q.append((j,ccx,ccy,1,cur))
                        visited[ccx][ccy]=1

                
                

    while(q):
        cur, x,y,dot,pre = q.popleft()
        # print("cur:",cur,"   x:",x,"  y:",y,"  dot:",dot,"   pre: ",pre)
        # print(visited[x][y])
        # print("==================")
        if [x,y]==[ix,iy]:
            answer=min(answer,visited[x][y])
            continue
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<=0 or ny<=0 or nx>50 or ny>50:
                continue
            if gr[nx][ny]==[]:
                continue
            if visited[nx][ny]<visited[x][y]+1:
                continue
            
            if dot==1:
                if inner[nx][ny][pre]==False:
                    if len(gr[nx][ny])>=2:
                        for j in gr[nx][ny]:
                            if j==cur:
                                continue
                            q.append((j,nx,ny,1,cur))
                            visited[nx][ny]=visited[x][y]+1
                    else:
                        q.append((cur,nx,ny,-1,cur))
                        visited[nx][ny]=visited[x][y]+1
            else:
                if len(gr[nx][ny])==1 and gr[nx][ny][0]==cur:
                    q.append((cur,nx,ny,-1,cur))
                    visited[nx][ny]=visited[x][y]+1

                if len(gr[nx][ny])>=2:
                    for j in gr[nx][ny]:
                        if j==cur:
                            continue
                        q.append((j,nx,ny,1,cur))
                        visited[nx][ny]=visited[x][y]+1
            
    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],3,4,7,8))

