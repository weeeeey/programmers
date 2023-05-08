
def solution(se):
    answer = 0
    n = len(se)
    for mid in range(1,n):
        left,right = mid-1,mid+1
        ord = 1
        while(left>=0 and right<n):
            if se[left]==se[right]:
                left-=1
                right+=1
                ord+=2
            else:
                break
        rrd=0

        left,right = mid,mid+1
        while(left>=0 and right<n):
            if se[left]==se[right]:
                left-=1
                right+=1
                rrd+=2
            else:
                break
        answer= max(answer,max(ord,rrd))
                
    return answer

print(solution("abaccaba"))
