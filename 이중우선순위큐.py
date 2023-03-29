import heapq

def solution(operations):
    answer = []
    q=[]
    for op in operations:
        a,b = op.split(" ")
        if(a=="I"):
            heapq.heappush(q,int(b))
        elif not q:
            continue
        elif(b=="-1"):
            heapq.heappop(q)
        else:
            heapq._heapify_max(q)
            heapq.heappop(q)
        print(q)
    if not q:
        answer=[0,0]
    else:
        answer=[max(q),q[0]]
    return answer

if __name__=='__main__':
    t=[]
    for i in range(9):
        t.append(input().rstrip()) 
    solution(t)

    