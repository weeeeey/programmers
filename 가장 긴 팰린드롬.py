
def solution(s):
    e = len(s)
    def find(s,start,end,ans):
        if(start<0 or end>e):
            return 1
        if (start>end):
            return ans
        if(end-start<ans):
            return ans
        mid = (start+end)//2
        left,right = mid-1,mid+1
        result = 1
        while(left>=0 and right<e):
            if s[left]==s[right]:
                result+=2
                left-=1
                right+=1 
            else:
                break
        result = max(result,ans)
        a = find(s,start,mid-1,result)
        b = find(s,mid+1,end,result)
        c = max(a,b)
        return max(result,c)
    
    answer = find(s,0,e,1)
    

        
    return answer

print(solution("abacde"))
