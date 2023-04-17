import heapq
INF = int(1e9)

def solution(n, s, a, b, fares):
    answer = INF
    gr = [[]for i in range(n+1)]
    for i in fares:
        st,et,c = i    
        gr[st].append([et,c])
        gr[et].append([st,c])
    distance = [[INF]*(n+1) for i in range(n+1)]

    def dikstra(start):
        q = []
        heapq.heappush(q,(0,start))
        distance[start][start]=0
        while(q):
            c,cur = heapq.heappop(q)    
            for nn in gr[cur]:
                next,cc = nn
                if distance[start][next]<=c+cc:
                    continue
                else:
                    distance[start][next]=c+cc
                    heapq.heappush(q,(distance[start][next],next))
    for i in range(1,n+1):
        dikstra(i)
    
    for i in range(1,n+1):
        answer=min(answer,distance[s][i]+distance[i][a]+distance[i][b])
    

    return answer

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))

# 예상되는 최저 택시요금은 다음과 같이 계산됩니다.
# 4→1→5 : A, B가 합승하여 택시를 이용합니다. 예상 택시요금은 10 + 24 = 34원 입니다.
# 5→6 : A가 혼자 택시를 이용합니다. 예상 택시요금은 2원 입니다.
# 5→3→2 : B가 혼자 택시를 이용합니다. 예상 택시요금은 24 + 22 = 46원 입니다.
# A, B 모두 귀가 완료까지 예상되는 최저 택시요금은 34 + 2 + 46 = 82원 입니다.