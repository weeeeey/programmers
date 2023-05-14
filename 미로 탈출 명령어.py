import heapq

dx = [1,0,0,-1]
dy = [0,-1,1,0]
# 하 좌 우 상
d = ['d', 'l', 'r', 'u']

def solution(n, m, sx, sy, ex, ey, k):
    answer = []
    
    visited = [[[[] for z in range(k+1)] for i in range(m+1) ] for j in range(n+1)]
    q = []
    heapq.heappush(q,(0,0,sx,sy))
    
    while(q):
        dist, cnt, x, y = heapq.heappop(q)
        if cnt==k and [x,y]==[ex,ey]:
            answer=visited[x][y][cnt]
            break
        if cnt+abs(ex-x)+abs(ey-y)>k:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cd = d[i]
            if nx<=0 or ny<=0 or nx>n or ny>m:
                continue
            if visited[nx][ny][cnt+1]!=[]:
                continue
            visited[nx][ny][cnt+1]=visited[x][y][cnt]+[cd]
            heapq.heappush(q,(dist+i+1,cnt+1,nx,ny))
    

    return "".join(answer) if answer else "impossible"

print(solution(3, 4, 2, 3, 3, 1, 5))
