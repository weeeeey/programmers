import heapq
from collections import deque

def dist_num():
    dx = [0,0,-1,1,1,1,-1,-1]
    dy = [-1,1,0,0,1,-1,1,-1]
    cell = [[0]*3 for i in range(4)]
    for i in range(3):
        for j in range(3):
            cell[i][j] = i*3+j+1
    cell[-1][0],cell[-1][2] = 11,11
    dist = [[100]*10 for i in range(10)]
    for i in range(4):
        for j in range(3):
            if cell[i][j]>10:
                continue
            t = cell[i][j]
            q = deque()
            q.append((0,i,j))
            dist[t][t]=1
            while(q):
                cnt,x,y = q.popleft()
                cur = cell[x][y]
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx<0 or ny<0 or nx>=4 or ny>=3:
                        continue
                    next = cell[nx][ny]
                    move = 2 if k<4 else 3
                    if next==11:
                        continue
                    if dist[t][next]<cnt+move:
                        continue
                    dist[t][next]= cnt+move
                    q.append((cnt+move,nx,ny))
    return dist
    

def solution(numbers):
    INF = int(1e9)
    answer = INF
    numbers = list(map(int,numbers))
    n=len(numbers)
    q = []
    d = dist_num()
    distant = [[INF,INF] for i in range(n)]
    distant[0][0]=d[4][numbers[0]]
    distant[0][1]=d[6][numbers[0]]
    heapq.heappush(q,(d[4][numbers[0]],numbers[0],6,1))
    heapq.heappush(q,(d[6][numbers[0]],4,numbers[0],1))
    while(q):
        dist,left,right,cur = heapq.heappop(q)
        if cur==n:
            return dist
        num = numbers[cur]
        l = dist+d[left][num]
        r = dist+d[right][num]
        
        if distant[cur][0]>l:
            heapq.heappush(q,(l,num,right,cur+1))
            distant[cur][0]=l
            
        if distant[cur][1]>r:
            heapq.heappush(q,(r,left,num,cur+1))
            distant[cur][1]=r


print(solution("1756"))