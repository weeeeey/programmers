import heapq

def solution(n, roads, sources, destination):
    gr = [[] for i in range(n+1)]
    INF = int(1e9)
    distance = [INF]*(n+1)
    distance[destination]=0
    answer = []
    for a,b in roads:
        gr[a].append(b)
        gr[b].append(a)
    
    q = []
    heapq.heappush(q,(0,destination))
    while(q):
        d, cur = heapq.heappop(q)
        for next in gr[cur]:
            if distance[next]<=d+1:
                continue
            distance[next]=d+1
            heapq.heappush(q,(d+1,next))
    for s in sources:
        if distance[s]!=INF:
            answer.append(distance[s])
        else:
            answer.append(-1)
    return answer
    

print(solution(5,   [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]],   [1, 3,5], 5))
        # 총 지역 수 , 왕복 가능한 길 정보,   각 부대원 위치 지역, 도착 지점
        # source의 순서대로 강철부대로 복귀 할 수 있는 최단 시간