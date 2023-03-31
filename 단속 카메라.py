def solution(routes):
    n = len(routes) #자동차 갯수
    answer = 1
    routes.sort(key=lambda x:(x[0],-x[1]))
    camera = [routes[0]]
    
    for route in routes:
        s,e = route
        
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))