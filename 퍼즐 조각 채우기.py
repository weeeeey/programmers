from collections import deque
from copy import deepcopy

# x,y = -1,2
# nx = y
# ny = -x  시계 방향으로 90도 회전 시 각 좌표의 변화
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def find_peace(gb):	#게임 보드에서 0으로 이뤄진 각 도형들의 좌표 모음을 찾아서 리턴
    n = len(gb)
    peace = []
    for i in range(n):
        for j in range(n):
            if gb[i][j]==0:
                q = deque()
                q.append((i,j))
                temp = [[0,0]]
                gb[i][j]=1
                while(q):
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx<0 or nx>=n or ny<0 or ny>=n:
                            continue
                        if gb[nx][ny]==0:
                            gb[nx][ny]=1
                            temp.append([nx-i,ny-j])
                            q.append((nx,ny))
                peace.append(temp)
    return peace

def solution(gb, table):
    answer = 0
    peace= find_peace(gb)
    n = len(gb)
    num = [[[0,0] for j in range(n)] for i in range(n)]
    temp = deepcopy(table)
    temp_num=1	# num이라는 그래프에 [도형 크기, 고유 번호] 를 입력하기 위한 과정
    for i in range(n):
        for j in range(n):
            if temp[i][j]==1:
                temp[i][j]=0
                m=1
                t = [[i,j]]
                q= deque()
                q.append((i,j))
                while(q):
                    x,y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0<=nx<n and 0<=ny<n and temp[nx][ny]==1:
                            m+=1
                            t.append([nx,ny])
                            temp[nx][ny]=0
                            q.append((nx,ny))
                for x,y in t:
                    num[x][y]=[m,temp_num]
                temp_num+=1

    complete = []
    for p in peace:	# 게임보드의 각 조각 탐색
        m = len(p)
        asd = False
        for i in range(n):
            if asd:
                continue                
            for j in range(n):
                if asd:
                    continue                
                if num[i][j][1] in complete:
                    continue
                if num[i][j][0]!=m:
                    continue
                NUM_T = num[i][j][1]
                pea = deepcopy(p)
                rot=0
                while(rot<=3):
                    tri = True
                    for x,y in pea:
                        nx = x + i
                        ny = y + j
                        if nx<0 or nx>=n or ny<0 or ny>=n or num[nx][ny][1]!=NUM_T:
                            tri = False
                            break
                    if tri:
                        complete.append(NUM_T)
                        asd=True
                        answer+=m
                        break
                    else:
                        rot+=1
                        for ri in range(m):
                            pea[ri][0],pea[ri][1] = pea[ri][1],-pea[ri][0]
        
    return answer

print(solution(
    [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]]	
,[[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]]
))