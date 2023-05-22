def find_parent(parents,unit):
    if parents[unit]==unit:
        return unit
    else:
        return find_parent(parents,parents[unit])

def solution(commands):
    answer = []
    gr = [[[] for i in range(51)] for j in range(51)]
    mer = [[[] for i in range(51)] for j in range(51)]
    
    voc = dict() # voca는 일반 딕셔너리
    for c in commands:
        temp = c.split(" ")
        cc = temp[0]
        if cc=="UPDATE":
            if len(temp)==4:
                x,y = map(int,temp[1:3])
                
                
            else:
                arr = voc[temp[1]]
                
                
        elif cc=="MERGE":
            sx,sy,ex,ey = map(int,temp[1:])
            
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