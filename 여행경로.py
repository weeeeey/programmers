from collections import deque

def solution(tickets):
    answer = []
    tickets.sort()
    n = len(tickets)
    gr = dict() #[출발점]:[출발점의 tickets idx]
    for i in range(n):
        s,e=tickets[i]        
        if not gr.get(s):
            gr[s]=[]
        gr[s].append(i)
    q = deque()
    q.append(("ICN",["ICN"],[]))
    while(q):
        cur, path, ticekt = q.popleft()

        if(len(path)==(n+1)):
            answer=path
            break
        if not gr.get(cur):
            continue
        for t in gr[cur]:
            if t in ticekt:
                continue
            end = tickets[t][1]
            q.append((end,path+[end],ticekt+[t]))
    return answer


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "SFO"], ["ATL","ICN"]]))