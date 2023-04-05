from collections import deque

def solution(a, b):
    answer = 0
    n = len(a)
    a.sort(reverse=True)
    b.sort(reverse=True)
    b=deque(b)
    idx = 0
    while(b and idx<n):
        cur = b.popleft()
        if a[idx]<cur:
            answer+=1
            idx+=1
        else:
            idx+=1
            b.appendleft(cur)
            

    return answer

print(solution([5,1,2,7],[2,2,6,8]))