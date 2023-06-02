# 플레이어 A가 초기 위치 (1, 0)에서 (1, 1)로 이동합니다. 
# 플레이어 A가 (0, 0)이나 (2, 0)으로 이동할 경우 승리를 보장할 수 없습니다.
# 따라서 무조건 이길 방법이 있는 (1, 1)로 이동합니다.
# 플레이어 B는 (1, 1)로 이동할 경우, 바로 다음 차례에
# A가 위 또는 아래 방향으로 이동하면 발판이 없어져 패배하게 됩니다. 
# 질 수밖에 없는 플레이어는 최대한 오래 버티도록 플레이하기 때문에
# (1, 1)로 이동하지 않습니다. (1, 2)에서 위쪽 칸인 (0, 2)로 이동합니다.
# A가 (1, 1)에서 (0, 1)로 이동합니다.
# B에게는 남은 선택지가 (0, 1)밖에 없습니다. 따라서 (0, 2)에서 
# (0, 1)로 이동합니다.
# A가 (0, 1)에서 (0, 0)으로 이동합니다. 이동을 완료함과 동시에 
# B가 서있던 (0, 1)의 발판이 사라집니다. B가 패배합니다.
# 만약 과정 2에서 B가 아래쪽 칸인 (2, 2)로 이동하더라도 A는 (2,
#  1)로 이동하면 됩니다. 이후 B가 (2, 1)로 이동, 다음 차례에 A가 
# (2, 0)으로 이동하면 B가 패배합니다.
# 위 예시에서 양 플레이어가 최적의 플레이를 했을 경우, 캐릭터의

#  이동 횟수 합은 5입니다. 최적의 플레이를 하는 방법은 여러 가지
# 일 수 있으나, 이동한 횟수는 모두 5로 같습니다.

from collections import deque

dx = [0,0,1,-1]
dy = [-1,1,0,0]

def check_dic(x,y,visited,b):
    possilbe = []
    n = len(b)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        num = nx*n + ny
        if nx<0 or ny <0 or nx>=n or ny>=n:
            continue
        if num in visited:
            continue
        if b[nx][ny]==0:
            continue
        else:
            possilbe.append([i])
    return possilbe

def solution(board, aloc, bloc):
    answer = -1
    n =len(board)
    visited = [[i for i in range(n*j,n*j+n)] for j in range(n)]
    a = aloc[0]*n+aloc[1]
    b = bloc[0]*n+bloc[1]
    q = deque()
    q.append((aloc[0],aloc[1],[a],0,bloc[0],bloc[1],[b],0))
    while(q):
        ax,ay,visite_a,a_cnt,bx,by,visite_b,b_cnt = q.popleft()
        a_possible = check_dic(ax,ay,visite_a,board)
        b_possible = check_dic(bx,by,visite_b,board)
        
        
            
            
    return answer

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]],[1, 0],[1, 2]	))