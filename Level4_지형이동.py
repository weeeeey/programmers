'''
문제 설명
N x N 크기인 정사각 격자 형태의 지형이 있습니다. 각 격자 칸은 1 x 1 크기이며, 숫자가 하나씩 적혀있습니다. 
격자 칸에 적힌 숫자는 그 칸의 높이를 나타냅니다.

이 지형의 아무 칸에서나 출발해 모든 칸을 방문하는 탐험을 떠나려 합니다. 칸을 이동할 때는 상, 하, 좌, 우로 한 칸씩 이동할 수 있는데, 
현재 칸과 이동하려는 칸의 높이 차가 height 이하여야 합니다. 높이 차가 height 보다 많이 나는 경우에는 사다리를 설치해서 이동할 수 있습니다. 
이때, 사다리를 설치하는데 두 격자 칸의 높이차만큼 비용이 듭니다. 따라서, 최대한 적은 비용이 들도록 사다리를 설치해서 모든 칸으로 이동 가능하도록 해야 합니다.
설치할 수 있는 사다리 개수에 제한은 없으며, 설치한 사다리는 철거하지 않습니다.

각 격자칸의 높이가 담긴 2차원 배열 land와 이동 가능한 최대 높이차 height가 매개변수로 주어질 때, 
모든 칸을 방문하기 위해 필요한 사다리 설치 비용의 최솟값을 return 하도록 solution 함수를 완성해주세요.

제한사항
land는 N x N크기인 2차원 배열입니다.
land의 최소 크기는 4 x 4, 최대 크기는 300 x 300입니다.
land의 원소는 각 격자 칸의 높이를 나타냅니다.
격자 칸의 높이는 1 이상 10,000 이하인 자연수입니다.
height는 1 이상 10,000 이하인 자연수입니다.
입출력 예
land	height	result
[[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]]	3	15
[[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]]	1	18
'''
# 같은 색끼리(사다리 사용 x) 묶은 다음에 각 색깔별로 이어지는 사다리 높이의 최소값들ㅇ르 저장하여 
# 크루누스 알고리즘을 이용해 한붓그리기를 할려함
# 로직은 알겠는데 테케가 몇개 틀림


# 우선순위 큐를 통해 가장 최소 가중치 경로로 이동함
# 이미 방문했던 곳이라면 안가버림


from sys import stdin 
import heapq
input = stdin.readline 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N = 0

def solution(land,height):
  global N
  N=len(land)
  q = []
  ans = 0 
  visited = [[False]*(N) for i in range(N)]
  heapq.heappush(q,(0,0,0))
  max_v = N*N
  visited_v = 0
  while(visited_v<max_v):
    w,x,y = heapq.heappop(q)
    if visited[x][y] == True:
      continue 
    visited[x][y] = True
    visited_v+=1
    ans+=w
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i] 
      if nx<0 or ny<0 or nx>=N or ny>=N:
        continue 
      value = abs(land[x][y]-land[nx][ny])
      if value<=height:
        heapq.heappush(q,(0,nx,ny))
      else:
        heapq.heappush(q,(value,nx,ny))
  return ans
