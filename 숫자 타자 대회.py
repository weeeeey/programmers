from collections import deque
import heapq

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
    d=dist_num()
    distant = [[[INF]*10 for i in range(10)] for j in range(n+1)]
    distant[0][4][6] = 0
    q = []
    heapq.heappush(q,(0,0,4,6))
    while(q):
        w, next, left, right = heapq.heappop(q)
        if next == n:
            return w
        num = numbers[next]

        if num in [left,right]:
            if distant[next+1][left][right]>w+1:
                distant[next+1][left][right]=w+1
                heapq.heappush(q,(w+1,next+1,left,right))
                
        else:
            if  distant[next+1][num][right]>w+d[left][num]:
                distant[next+1][num][right]=w+d[left][num]
                heapq.heappush(q,(w+d[left][num],next+1,num,right))
            if  distant[next+1][left][num]>w+d[right][num]:
                distant[next+1][left][num]=w+d[right][num]
                heapq.heappush(q,(w+d[right][num],next+1,left,num))

    return answer
            

print(solution("1756"))
