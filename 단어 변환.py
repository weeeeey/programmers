from collections import deque

def solution(begin, target, words):
    if(target not in words):
        return 0
    words=[begin]+words
    end = words.index(target)
    n = len(words)
    k=len(begin)
    visited=[False]*n
    gr = [[]for i in range(n)]
    for i in range(n):
        cur = words[i]
        for j in range(i+1,n):
            next = words[j]
            dif = 0
            for z in range(k):
                if cur[z]!=next[z]:
                    dif+=1
                if dif>=2:
                    break
            if dif==1:
                gr[i].append(j)
                gr[j].append(i)
    
    q=deque()
    q.append((0,0))
    visited[0]=True
    while(q):
        cur,cnt = q.popleft()
        for next in gr[cur]:
            if visited[next]==True:
                continue
            if next==end:
                return cnt+1
            visited[next]=True
            q.appendleft((next,cnt+1))
    return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))