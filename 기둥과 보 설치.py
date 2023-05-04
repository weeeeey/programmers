# 기둥 위치
    # 바닥 위 
    # 보의 한쪽 끝 부분 위
    # 다른 기둥 위
    # 기둥은 위로
    
# 보 위치
    # 한쪽 끝 부분이 기둥 위에 위
    # 양쪽 끝 부분이 다른 보와 동시 연결
    # 보는 오른쪽으로 
    
# 기둥과 보의 삭제 규칙도 위와 같음

# x,y,a,b
# xy는 기둥 보를 설치or삭제 할 교차점
# a가 0이면 기둥, 1이면 보
# b가 0이면 삭제, 1은 설치

from collections import deque

dy = [1,0] # a가 0 이면 행 아래로
dx = [0,1]  # a가 1이면 열 오른

def solution(n,build):
    gr = [[[[[False,False] for i in range(n+1)] for j in range(n+1)]for k in range(n+1)] for z in range(n+1)]
    x,y,a = build[0][0],build[0][1],0
    nx, ny = x+dx[a], y+dy[a]
    gr[y][x][ny][nx][0]=True
    install = [[[False,False] for i in range(n+1)] for j in range(n+1)]
    install[y][x][0]=True
    install[ny][nx][0]=True
    q = deque()
    q.append([x,y,a])
    answer = [[x,y,a]]
    
    for i in range(1,len(build)):
        x,y,a,b = build[i]
        print(x,y,a,b)
        nx = x + dx[a]
        ny = y + dy[a]
        if b == 1:
            if a==0:
                if y==0 or ny==0 or install[y][x][0]==True or install[y][x][1]==True:
                    install[ny][nx][0]=True
                    gr[y][x][ny][nx][0]=True
                    print(x,y,nx,ny,"기둥")
            else:
                if install[y][x][0]==True or install[ny][nx][0]==True or (install[y][x][1]==True and install[ny][nx][1]==True):
                    install[y][x][1]=True
                    install[ny][nx][1]=True
                    gr[y][x][ny][nx][1]=True
                    print(x,y,nx,ny,"보")

    for i in range(n+1):
        print(install[i])
    while(q):
        x,y,a = q.popleft()
        
        nx = x + dx[a]
        ny = y + dy[a]
        
    return answer

print(solution(5,[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))


# def solution(n, build):
#     answer = []
#     gr = [[[False,False] for j in range(n+1)] for i in range(n+1)]
#     # x,y의 [0] 은 기둥이 트루인지, [1]은 보가 트루인지 체크
#     x,y = build[0][0]+dx[0],build[0][1]+ dy[0]
#     gr[y][x][0]=True
#     gr[build[0][1]][build[0][0]][0]=True
#     for i in range(1,len(build)):
#         x,y,a,b = build[i]
#         nx = x + dx[a]
#         ny = y + dy[a]
#         if b == 1:
#             if a == 1:
#                 if gr[y][x][0]==True or gr[ny][nx][0]==True or (gr[y][x][1]==True and gr[ny][nx][1]==True):
#                     gr[ny][nx][1]=True
#                     gr[y][x][1]=True
#             else:
#                 if y==0 or gr[y][x][0]==True or gr[y][x][1]==True or gr[ny][nx][1]==True:
#                     gr[ny][nx][0]=True
#                     gr[y][x][0]=True
#         else:
#             if gr[ny][nx][a]==True:
#                 gr[ny][nx][a]=False
#                 if [x,y,a] in answer:
#                     answer.remove([x,y,a])
#     sy,sx,dic = build[0][1], build[0][0], build[0][2]
#     q = deque()
#     q.append((sx,sy,dic))
#     while(q):
#         x,y,d = q.popleft()
#         answer.append([x,y,d])
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if gr[ny][nx] == [False,False]:
#             continue
#         if gr[ny][nx][1]==True:
#             q.append((nx,ny,1))
#         else:
#             q.append((nx,ny,0))
        
#     answer.sort()
#     return answer
