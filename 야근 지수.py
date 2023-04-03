import heapq

def solution(n, works):
    if(sum(works)<=n):
        return 0
    answer = 0
    q = []
    for i in range(len(works)): 
        heapq.heappush(q,(-works[i]))
    while(n!=0):
        max_n = heapq.heappop(q)*(-1)
        max_n-=1
        n-=1
        heapq.heappush(q,(-max_n))
    for i in range(len(q)):
        answer+=q[i]**2
    return answer

    
print(solution(4,[4,3,3]))