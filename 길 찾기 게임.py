#   x,y 좌표
# x는 모두 다른 값, y는 레벨, 자식 노드는 부모 노드보다 y값이 작음
# V의 X > V의 왼쪽 서브 트리 x
# V의 X < V의 오른쪽 서브 트리 x



def solution(info): #info len <10,000
    answer = [[]]
    n = len(info)
    temp = [[info[i][0],info[i][1],i+1] for i in range(n)]  # x,y,index
    temp.sort(key=lambda x:(-x[1],x[0]))
    print(temp)
    

    return answer
    # 전위 순회, 후위 순회 결과 return


# [[8, 6], [3, 5], [11, 5], [1, 3], [5, 3], [13, 3], [2, 2], [7, 2], [6, 1]]
#    7       4       2         6       1       3        9       8       5

#   전위 순회 : 7, 4, 6, 9, 1, 8, 5, 2, 3
#   후위 순회 : 9, 6, 5, 8, 1, 4, 3, 2, 7





print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))
                # 1     2      3      4     5     6     7     8     9