# D 2: x에서 2 down
# U 2:x에서 2 up
# C : x 삭제
# Z : 가장 최근 삭제 된 것들 복구 (복구 시 x가 아닌 원래 자리로 )(삭제 할 때 위치도 저장해야함)

# n <= 1,000
def solution(n, pivot, cmd):
    answer = ''
    gr = dict()
    for i in range(n):
        gr[i] = [i-1,i+1]
    gr[0][0]="False"
    gr[n-1][1]="False"
    
    garbage = []
    for c in cmd:
        if len(c)==1:
            if c == "Z":
                key,left,right = garbage.pop()
                gr[key]=[left,right]
                if left=="False":
                    gr[right][0]=key
                elif right=="False":
                    gr[left][1]=key
                else:
                    gr[left][1]=key
                    gr[right][0]=key
                
            else:
                left,right = gr[pivot]
                if left=="False":
                    gr[right][0]="False"
                    del gr[pivot]
                    garbage.append([pivot,left,right])
                    pivot=right
                elif right=="False":
                    gr[left][1]="False"
                    del gr[pivot]
                    garbage.append([pivot,left,right])
                    pivot=left
                else:
                    gr[left][1]=right
                    gr[right][0]=left
                    del gr[pivot]
                    garbage.append([pivot,left,right])
                    pivot=right
                    
        else:
            dic, move  = c.split(" ")
            move = int(move)
            if dic=="D":
                for i in range(move):
                    pivot=gr[pivot][1]
            else:
                for i in range(move):
                    pivot=gr[pivot][0]
                
    answer=["X"]*n
    for k in gr:
        answer[k]="O"
    answer= "".join(answer)
    return answer

print(solution(8,
                2,
                ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))
# ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))