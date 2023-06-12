def solution(n, light):
    answer = 0
    num = [0]*(n+1)
    gr = [[] for i in range(n+1) ]
    for x,y in light:
        gr[x].append(y)
        gr[y].append(x)
        num[x]+=1
        num[y]+=1
    print(num[1:])
    
    return answer


print(solution(8,[[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))