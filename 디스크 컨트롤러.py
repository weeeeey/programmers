# jobs의 길이는 1 이상 500 이하입니다.
# jobs의 각 행은 하나의 작업에 대한 [작업이 요청되는 시점, 작업의 소요시간] 입니다.
# 각 작업에 대해 작업이 요청되는 시간은 0 이상 1,000 이하입니다.
# 각 작업에 대해 작업의 소요시간은 1 이상 1,000 이하입니다.
# 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
import heapq

def solution(jobs):
    jobs.sort()
    n = len(jobs)
    answer, time, cur = 0,0,0   #구하고자 하는 작업량, 작업을 통한 현재 시간, 현재 노드
    start = -1
    q = []
    while(cur<n):
        for next in jobs:
            if start<next[0]<=time:
                heapq.heappush(q,(next[1],next[0]))
        if(len(q)>0):
            node = heapq.heappop(q)
            start=time
            time+=node[0]
            answer+=time-node[1]
            cur+=1
        else:
            time+=1
    return answer//n
    

print(solution([[0, 3], [1, 9], [2, 6]]))