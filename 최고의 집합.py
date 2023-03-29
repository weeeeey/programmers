def solution(n, s):
    a=s//n
    b=s%n
    l = [a]*n
    for i in range(-1,-b-1,-1):
        l[i]+=1
    if(l[0]==0):
        return [-1]
    return l



if(__name__=="__main__"):
    n,s = map(int,input().rsplit())
    print(solution(n,s))