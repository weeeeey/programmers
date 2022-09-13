# 기본적인 로직인 O(n^2) 이면 정확성은 통과 가능
# 스킬의 데이터가 250,000 이라 매번 전체 그래프를 탐색하면 1000*1000*250,000 이 되어서 시간 초과임
# 이를 해결하기 위해 전체 그래프를 매번 탐색하는 것이 아닌 해당 영역들의 누적된 가중치를 저장할 방법이 필요했음

# 이것은 누적합 알고리즘을 통해 해결 가능
# 기본적으로 0으로 가득찬 리스트 선언
# [0]부터 [3]까지 K를 빼고 싶다면 위 리스트에 K를 뺴면 되는데
# List[0] -= k
# List[4] -= k
# 그 후 다음으로 빼고 싶은 수들을 계속해서 위와 같은 방법으로 인덱스에 저장하면 됨

# 모두 끝난 후 0부터 마지막 인덱스까지 이전 값을 더해준다면 누적합이 되어버림
# 나온 누적합 리스트를 그래프에 더해주면 끝



def solution(board, skill):
    answer = 0
    n,m = len(board),len(board[0])
    gr = [[0]*(m+1) for i in range(n+1)]
    for s in skill:
        a,sx,sy,ex,ey, d = s
        d=-d if a==1 else d
        gr[sx][sy]+=d
        gr[sx][ey+1]-=d
        gr[ex+1][sy]-=d
        gr[ex+1][ey+1]+=d

    for i in range(n+1):
        for j in range(1,m+1):
            gr[i][j]+=gr[i][j-1]
    for i in range(0,m+1):
        for j in range(1,n+1):
            gr[j][i] = gr[j][i]+gr[j-1][i]
    print(gr)
    for i in range(n):
        for j in range(m):
            if board[i][j]+gr[i][j]>0:
                answer+=1
        
    return answer

a = [[1,2,3],[4,5,6],[7,8,9]]
b = [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]
print(solution(a,b))
