# D 2: x에서 2 down
# U 2:x에서 2 up
# C : x 삭제
# Z : 가장 최근 삭제 된 것들 복구 (복구 시 x가 아닌 원래 자리로 )(삭제 할 때 위치도 저장해야함)

# n <= 1,000
def solution(n, pivot, cmd):
    answer = ''
    arr = [i for i in range(n)]
    delete = [True]*n
    garbage = []    
    for c in cmd:
        if len(c)==1:
            if c == "Z":
                num = garbage.pop()
                
            else:
                tri = False
                for i in range(pivot+1,n):
                    if delete[i]==True:
                        pivot=i
                        tri = True
                        break
                if tri == False:
                    pivot
        else:
            dic, move  = c.split(" ")
            if dic=="D":
                pivot+=int(move)
                if pivot>=len(arr):
                    pivot=len(arr)-1
            else:
                pivot-=int(move)
                if pivot<=0:
                    pivot=1
    print(arr)

    
        
    return answer

print(solution(8,
                2,
                ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))
# ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))