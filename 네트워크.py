from collections import deque

def solution(n, computers):
    answer = 0
    visited = [False]*n
    gr = [[] for i in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if computers[i][j]==1:
                gr[i].append(j)
                gr[j].append(i)
    for i in range(n):
        if visited[i]==True:
            continue
        answer+=1
        visited[i]=True
        q = deque()
        q.append(i)
        while(q):
            cur = q.popleft()
            for next in gr[cur]:
                if visited[next]==True:
                    continue
                visited[next]=True
                q.append(next)

    return answer
    

if __name__=='__main__':
    n = int(input().rstrip())
    com = []
    while(True):
        op = list(map(int,input().rsplit()))
        if not op:
            break
        com.append(op)
    print(solution(n,com))
