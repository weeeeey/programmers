import heapq
INF = int(1e9)

def solution(n, edge):
    answer = 0
    gr = [[]for i in range(n+1)]
    dit = [INF]*(n+1)
    dit[1]=0
    q = []
    for s,e in edge:
        gr[s].append(e)
        gr[e].append(s)
    heapq.heappush(q,(0,1))
    m=0
    while(q):
        dd, cur = heapq.heappop(q)
        for next in gr[cur]:
            d = dd+1
            if dit[next]>d:
                dit[next]=d
                heapq.heappush(q,(d,next))
                m=max(m,d)

    return dit.count(m)

print(solution(6,[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))