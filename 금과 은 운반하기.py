def solution(a, b, g, s, w, t):
    answer = -1
    n = len(g)
    check = [0]*n
    num=0
    return answer

print(solution(90,500,[70,70,0],[0,0,500],[100,100,2],[4,8,1],499))

# 어느 왕국에 하나 이상의 도시들이 있습니다
# 왕국의 왕은 새 도시를 짓기로 결정하였습니다
# 해당 도시를 짓기 위해서는 도시를 짓는 장소에 
# 금 a kg과 은 b kg이 전달되어야 합니다.
# 
# 각 도시에는 번호가 매겨져 있는데, i번 도시에는 금
#  g[i] kg, 은 s[i] kg, 그리고 트럭 한 대가 있습니다
# i번 도시의 트럭은 오직 새 도시를 짓는 건설 장소와
#  i번 도시만을 왕복할 수 있으며, 편도로 이동하는 데 t[i] 시간이 걸리고, 
#  최대 w[i] kg 광물을 운반할 수 있습니다
# (광물은 금과 은입니다
# 
# 즉, 금과 은을 동시에 운반할 수 있습니다.) 모든 트럭은 같은 도로를 
# 여러 번 왕복할 수 있으며 연료는 무한대라고 가정합니다.