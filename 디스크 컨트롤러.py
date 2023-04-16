import heapq

def solution(jobs):
    answer = 0  # 각 작업의 요청부터 종료까지 걸린 시간
    result = 0  # 총 작업 시간
    q = []
    for i in jobs:
        a,b = i
        heapq.heappush(q,(a+b,a))
    while(q):
        end,start = heapq.heappop(q)
        job = end-start
        answer+=(abs(result-start)+job)
        result+=job
    
    return answer//len(jobs)

print(solution([[0, 3], [1, 9], [2, 6]]))