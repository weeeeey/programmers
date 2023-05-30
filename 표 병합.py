def find_parent():
    return 0

def solution(commands):
    answer = []
    gr = [[[] for i in range(51)] for j in range(51)]
    mer = [[[0] for i in range(51)] for j in range(51)]
    mer_num = [[] for j in range(51)]
    num=1
    voc = dict() # voca는 일반 딕셔너리
    
    
    for c in commands:
        temp = c.split(" ")
        cc = temp[0]
        if cc=="UPDATE":
            if len(temp)==4:
                x,y = map(int,temp[1:3])
                
                
            else:
                print(temp[1])
                
                
        elif cc=="MERGE":
            sx,sy,ex,ey = map(int,temp[1:])
            le = 0
            if mer[sx][sy]==0 and mer[ex][ey]==0:
                mer[sx][sy]=num
                mer[ex][ey]=num
                mer_num.append([sx,sy])
                mer_num.append([ex,ey])
                num+=1
            elif mer[sx][sy]!=0 and mer[ex][ey]!=0:
                t= mer[sx][sy]
                for i in range(le):
                    x,y = mer_num[t][i]
                    mer[x][y]=t
                    mer_num[t].append([x,y])
            else:
                t = mer[sx][sy] if mer[sx][sy] else mer[ex][ey]
                le = len(mer_num[t])                
                for i in range(le):
                    x,y = mer_num[t][i]
                    mer[x][y]=t
                    mer_num[t].append([x,y])
            if gr[sx][sy]!=[]:
                gr[ex][ey]=gr[sx][sy]
            elif gr[ex][ey]!=[]:
                gr[sx][sy]=gr[ex][ey]
            

        elif cc=="PRINT":
            answer.append(gr[int(temp[1])][int(temp[2])])
        else:
            x,y = map(int,temp[1:])
            
    # print(gr[1][3])
    # print(gr[1][4])
    # print(voc)
    return answer

print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", 
                "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean",
                "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", 
                "UPDATE 3 2 korean", "UPDATE 3 3 noodle", 
                "UPDATE 3 4 instant", "UPDATE 4 1 pasta", 
                "UPDATE 4 2 italian", "UPDATE 4 3 noodle", 
                "MERGE 1 2 1 3", "MERGE 1 3 1 4", 
                "UPDATE korean hansik", "UPDATE 1 3 group", 
                "UNMERGE 1 4", 
                "PRINT 1 3", "PRINT 1 4"]
            ))