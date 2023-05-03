# 규칙에 따라 풍선이 1개만 남을 때까지 터트리기
    # 인접한 두 풍선 고른 뒤,하나를 터트림
    # 터져서 생긴 빈 공간을 없애기 위해 중앙으로 밀착
        # 번호가 작은 풍선을 1번만 터트릴 수 있음
        # 이후에는 큰 풍선 터트리기
# 어떤 풍선은 마지막까지 남는 것이 불가능 할 수 있음
# 최후까지 남는게 가능한 풍선 개수 리턴

# cur 기준 왼쪽에서의 최솟값을 구함.
    # 왼쪽 최솟값이 cur 보다 클 경우 그냥 성공
    # 왼쪽 최솟값이 cur 보다 작을 경우 
        # 오른쪽으로 이동하면서 cur 보다 작은 값 나오면 break
        # 끝에 도달하면 생존

def solution(a):
    answer = 2
    n = len(a)
    min_arr = [0]*n
    min_arr[0]=a[0]
    min_arr[-1]=a[-1]
    arr = [a[0]]*n
    
    for i in range(-2,-n,-1):
        if a[i]>min_arr[i+1]:
            min_arr[i]=min_arr[i+1]
        else:
            min_arr[i]=a[i]
    for i in range(1,n):
        if a[i] < arr[i-1]:
            arr[i]=a[i]
        else:
            arr[i]=arr[i-1]

    for i in range(1,n-1):
        if a[i]<arr[i-1]:
            answer+=1
        else:
            if a[i]>min_arr[i+1]:
                continue
            else:
                answer+=1

    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))