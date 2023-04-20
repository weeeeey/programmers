def solution(s, k):
    answer = 0
    start = 0
    end = max(s)
    while(start<=end):
        mid = (start+end)//2
        cnt = 0
        for temp in s:
            if temp<=mid:
                cnt+=1
            else:
                cnt=0
            if cnt>=k:    
                end=mid-1    
                break
        
        if cnt<k:
            start=mid+1
            
        

    return start


# k개로 묶여진 묶음을 찾고 그 묶음 중의 최댓값이 가장 작은 값을 찾기 

# k번째로 작은 수를 찾기? => 실패


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))

# k개로 묶여진 묶음을 찾고 그 묶음 중의 최댓값이 가장 작은 값을 찾기 

# k번째로 작은 수를 찾기? => 실패
