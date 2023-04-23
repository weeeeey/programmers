# key: m*m 열쇠, 회전 이동 가능 - 열쇠의 돌기를 자물쇠 홈에 딱 맞게 하면 열림
# lock: n*n 자물쇠
# 3<=n,m<=20
# 0 홈, 1 돌기

# 열쇠의 돌기(1)-> 자물쇠 홈(0) 0
# 자물쇠 영역 벗어난 열쇠 영역은 영향x
# 자물쇠 영역 안에선 열쇠의 돌기(1) -> 자물쇠 돌기(1) x
# 자물쇠 모든 홈을 채워 비는 곳이 없어야 성공

# lock 에서 반복문을 통해 첫 1과 마지막 1을 찾은 후 좌표 저장
# 해당 좌표를 통해 범위 지정 후 옮겨가며 key에 대입해서 찾기

from copy import deepcopy


dx = [1,0]
dy = [0,1]

def solution(ori, lock):
    answer = True
    m,n = len(ori),len(lock) 
    if n>m:
        return False
    start = [-1,-1]
    end = [-1,-1]
    t = []  #lock의 0값 저장
    for i in range(n):
        for j in range(m):
            if lock[i][j]==0:
                t.append([i,j])
                end=[i,j]
                if start==[-1,-1]:
                    start=[i,j]
    sx = start[0]
    sy = start[1] if start[1]<end[1] else end[1]
    ex = end[0]
    ey = end[1] if start[1]<end[1] else start[1]
    
    for k in range(4):
        if k!=0:
            gr = [[0]*m for i in range(m)]
            for j in range(m):
                for i in range(m):
                    gr[i][j] = ori[m-1-j][i]
            ori=deepcopy(gr)
        q = dequ
                    
    return answer

print(solution([[0, 0, 0], [1, 0,0], [0, 1, 1]],
                #열쇠
            [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
            #자물쇠