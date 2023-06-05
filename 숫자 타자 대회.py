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
    answer = 0
    numbers = list(map(int,numbers))
    n=len(numbers)
    
    m = n if n%2==0 else n-1
    d = dist_num()
    q = []
    heapq.heappush(q,(0,4,6,0))
    while(q):
        dist,left,right,num = heapq.heappop(q)
        if num==m:
            answer=-dist
            continue
        a,b = numbers[num],numbers[num+1]
        one = d[left][a] + d[a][b]
        heapq.heappush(q,(dist-one,b,right,num+2))
        two = d[left][a] + d[right][b]
        heapq.heappush(q,(dist-two,a,b,num+2))
        three = d[right][a] + d[left][b]
        heapq.heappush(q,(dist-three,b,a,num+2))
        four = d[right][a] + d[a][b]
        heapq.heappush(q,(dist-four,left,b,num+2))
    if n!=m:
        a = answer+d[left][numbers[-1]]
        b = answer+ d[right][numbers[-1]]
        answer=min(a,b)
    return answer

print(solution("1756"))