from collections import deque

INF = int(1e9)
#상,하,좌,우
dx = [-1,1,0,0] #k가 0,1 이면 q에 방향 0 넣어주기
dy = [0,0,-1,1] #k가 2,3 이면 q에 방향 1 넣어주기

def solution(gr):
    answer = INF
    n = len(gr)
    cost = [[[INF]*4 for j in range(n)] for i in range(n)]
    cost[0][0]=[0,0,0,0]
    q=deque()
    			# 0,0에서의 첫 이동 지점인 (0,1)과 (1,0)을 큐에 먼저 넣어줌
    for xx,yy in [[0,1],[1,0]]:
        if gr[xx][yy]==1:
            continue
        if([xx,yy]==[1,0]):
            a,b,c=0,1,1
        else:
            a,b,c=1,3,3
        cost[xx][yy][b]=100
        q.append((xx,yy,a,c))
    while(q):
    				# x,y좌표, 직선인지 판별할 dic, 현재 위치 왔을때의 방향
        x,y,dic,before = q.popleft()
        if([x,y]==[n-1,n-1]):
            answer=min(answer,cost[x][y][before])
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if gr[nx][ny]==1:
                continue
            nextDic = 0 if i in [0,1] else 1 #[0,1]은 dx,dy에서의 (-1,0),(1,0)을 뜻함(상하). 좌우라면 1
            c = 600 if nextDic!=dic else 100
            if cost[nx][ny][i]<cost[x][y][before]+c:
                continue
            cost[nx][ny][i]=cost[x][y][before]+c
            q.append((nx,ny,nextDic,i))
    return answer
            

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))