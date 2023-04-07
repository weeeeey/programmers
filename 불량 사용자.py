from collections import deque

def solution(u_id, b_id):
    answer = []
    n = len(b_id)
    kk = len(u_id)
    gr = [[] for i in range(n)]
    for i in range(n):
        cur = b_id[i]
        m = len(cur)
        for j in range(kk):
            if(len(u_id[j])!=m):
                continue
            z = False
            for k in range(m):
                if(cur[k]=="*"):
                    continue
                if(u_id[j][k]!=cur[k]):
                    z=True
                    break
            if(z==False):
                gr[i].append(j)
    q = deque()
    for i in gr[0]:
        q.append((1,[i]))
    while(q):
        num, cur = q.popleft()
        if(num==n):
            answer.append(cur)
            continue
        for i in gr[num]:
            if i in cur:
                continue
            else:
                q.append((num+1,cur+[i]))
    print(answer)
    a = set([tuple(set(item))for item in answer])
    return len(a)





print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"]))