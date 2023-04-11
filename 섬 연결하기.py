import heapq
INF = int(1e9)

def findParent(cur,par):
    if par[cur]==cur:
        return cur
    return findParent(par[cur],par)

def solution(n, costs):
    answer= 0
    costs.sort(key=lambda x:x[2])
    parent = [i for i in range(n)]
    num = 0
    for cost in costs:
        s,e,c = cost    
        S = findParent(s,parent)
        E = findParent(e,parent)
        if (S==E):
            continue
        else:
            if(S<E):
                parent[E]=S
            else:
                parent[S]=E
            answer+=c
            num+=1
        if(num==(n-1)):
            break
            
    return answer

print(solution(4,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))