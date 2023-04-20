# gems len 100,000 이하
def solution(gems):
    answer = [0,len(gems)]
    result = len(gems)
    w = list(set(gems))
    cnt = dict()
    for i,ddd in enumerate(w):
        cnt[ddd]=0
    n = len(gems)
    nn = len(w)
    if(nn==1):
        return [1,1]
    start,end =0,0
    cnt[gems[end]]=1
    r=1
    while(start<n and end<n):
        if(r==nn):
            if (end-start<result):
                answer=[start,end]
                result=end-start
            else:
                cnt[gems[start]]-=1
                if cnt[gems[start]]==0:
                    r-=1
                start+=1
        else:
            end+=1
            if(end==n):
                break
            cnt[gems[end]]+=1
            if(cnt[gems[end]])==1:
                r+=1
    
    return [answer[0]+1,answer[1]+1]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))