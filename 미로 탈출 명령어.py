import heapq

dx = [-1,0,0,1]
dy = [0,-1,1,0]
dy = [0,1,-1,0]
d = ['u', 'r', 'l', 'd']

def solution(n, m, sx, sy, ex, ey, k):
    answer = []
    q = []
    gr = [[0]*(m+1) for i in range(n+1)]
    heapq.heappush(q,(0,0,sx,sy,[]))
    while(q):
        dist, cnt, x, y,dir = heapq.heappop(q)
        if cnt==k and [x,y]==[ex,ey]:
            answer=dir
            break
        if cnt+abs(ex-x)+abs(ey-y)>k:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cd = d[i]
            if nx<=0 or ny<=0 or nx>n or ny>m:
                continue
            if dist-i-1>gr[nx][ny]:
                continue
            gr[nx][ny]=dist-i-1
            heapq.heappush(q,(dist-i-1,cnt+1,nx,ny,dir+[cd]))
    

    return "".join(answer) if answer else "impossible"

print(solution(3, 4, 2, 3, 3, 1, 5))
