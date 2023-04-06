# 응모한 사용자 아이디들은 서로 중복되지 않습니다.
# 불량 사용자 아이디 하나는 응모자 아이디 중 하나에 해당하고 같은 응모자 아이디가 중복해서 제재 아이디 목록에 들어가는 경우는 없습니다.
# 제재 아이디 목록들을 구했을 때 아이디들이 나열된 순서와 관계없이 아이디 목록의 내용이 동일하다면 같은 것으로 처리하여 하나로 세면 됩니다.
from collections import deque

def solution(u_id, b_id):
    answer = []
    n = len(b_id)
    gr = [[] for i in range(n)]
    for i in range(n):
        cur = b_id[i]
        m = len(cur)
        for j in range(len(u_id)):
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
                gr[i].append(u_id[j])
    q = deque()
    for i in gr[0]:
        q.append((1,[i]))

    while(q):
        num, cur = q.popleft()
        if (num==n):
            answer.append(cur)
            continue
        for i in gr[num]:
            if i in cur:
                continue
            else:
                q.append((num+1,cur+[i]))
    a = list(set([tuple(set(item))for item in answer]))
    
    return len(a)



print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"]))