'''
문제 설명

출발지점부터 distance만큼 떨어진 곳에 도착지점이 있습니다. 
그리고 그사이에는 바위들이 놓여있습니다. 바위 중 몇 개를 제거하려고 합니다.
예를 들어, 도착지점이 25만큼 떨어져 있고, 
바위가 [2, 14, 11, 21, 17] 지점에 놓여있을 때 바위 2개를 제거하면 출발지점, 
도착지점, 바위 간의 거리가 아래와 같습니다.
제거한 바위의 위치 	각 바위 사이의 거리 	거리의 최솟값
[21, 17] 	[2, 9, 3, 11] 	2
[2, 21] 	[11, 3, 3, 8] 	3
[2, 11] 	[14, 3, 4, 4] 	3
[11, 21] 	[2, 12, 3, 8] 	2
[2, 14] 	[11, 6, 4, 4] 	4

위에서 구한 거리의 최솟값 중에 가장 큰 값은 4입니다.

출발지점부터 도착지점까지의 거리 distance, 
바위들이 있는 위치를 담은 배열 rocks, 제거할 바위의 수 n이 매개변수로 주어질 때, 
바위를 n개 제거한 뒤 각 지점 사이의 거리의 최솟값 중에 
가장 큰 값을 return 하도록 solution 함수를 작성해주세요.
제한사항

    도착지점까지의 거리 distance는 1 이상 1,000,000,000 이하입니다.
    바위는 1개 이상 50,000개 이하가 있습니다.
    n 은 1 이상 바위의 개수 이하입니다.

입출력 예
distance 	rocks 	n 	return
25 	[2, 14, 11, 21, 17] 	2 	4
'''
# 문제의 데이터 범위가 넓기 때문에 조합으로 모든 경우의 수를 구해보는 것은 옳지 못함
# dp 로 최적의 수를 구해야하나 생각해봤지만 돌 갯수가 5만개라서 이것 또한 패스
# 최소로 올 수 있는 distance를 기준으로 이분 탐색을 진행

# 초기 돌과 그 다음 돌의 거리를 계산하여 mid 보다 작다면 그 돌을 제거한다고 생각해서
# 제거 갯수 +1 다음 인덱스와 현재 기준 돌 거리를 계산해줌 
# (거리 차가 더 작다는 것은 기준인 최소값보다 더 작은 것이므로) 
# 갯수가 n을 초과했다면 더 많이 제거한 것이므로 False 리턴

def binary(rock,middle, n):
  temp = 0
  start= 0
  idx = 0
  while(idx<len(rock)):
    if rock[idx]-start<middle:
      temp+=1
      idx+=1
      if temp>n:
        return False
    else:
      start = rock[idx]
      idx+=1
  return True

def solution(distance, rocks, n):
  rocks.sort()
  rocks.append(distance)
  start = 1
  end = distance
  ans = 0
  while (start < end):
      mid = (start + end) // 2
      temp = binary(rocks,mid, n)
      if temp == True:
          start = mid + 1
          ans = mid
      else:
          end = mid
  return ans
