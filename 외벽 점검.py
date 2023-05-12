from bisect import bisect_left
from collections import deque
from itertools import permutations

# arr = [1,3,4,9,10,13,15,16,21,22]
# print(bisect_left(arr,4))


def solution(n, weak, dist):
    answer = 9
    w = len(weak)
    q = deque()
    dist.sort(reverse=True)
    dists = list(permutations(dist,len(dist)))
    for i in range(w):
        weak.append(weak[i]+n)
        

    for dis in dists:
        for i in range(w):
            q.append((0,i,0))
        while(q):
            cnt, cur_idx, d_idx = q.popleft()

            if cnt==w:
                answer=min(answer,d_idx)
                continue
            if cur_idx>=w or d_idx>=len(dist):
                continue
            
            cur,d = weak[cur_idx], dis[d_idx]
            end= cur+d
            e_idx = bisect_left(weak,end)
            temp = e_idx-cur_idx
            if weak[e_idx]==end:
                q.append((cnt+temp+1,e_idx+1,d_idx+1))
            else:
                q.append((cnt+temp,e_idx,d_idx+1))
        
    return answer if answer!=9 else -1

    
print(solution(	12, [1, 3, 4, 9, 10], [3, 5, 7]))