
def solution(routes):
    n = len(routes) #자동차 갯수
    answer = 1
    routes.sort(key=lambda x:x[1])
    camera = routes[0][1]
    for i in range(1,n):
        s,e = routes[i]
        if camera<s:
            camera=e
            answer+=1
        else:
            continue
    
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))