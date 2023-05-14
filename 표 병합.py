def solution(commands):
    answer = []
    n,m = 50,50
    gr = [[[] for i in range(51)] for j in range(51)]
    mer = dict() # merge는 리스트 
    voc = dict() # voca는 일반 딕셔너리
    for c in commands:
        temp = c.split(" ")
        cc = temp[0]
        if cc=="UPDATE":
            if len(temp)==4:
                x,y = int(temp[1]),int(temp[2])
                gr[x][y] = temp[3]
                if voc.get(temp[3]):
                    voc[temp[3]].append([x,y])
                else:
                    voc[temp[3]] = [[x,y]]
            else:
                arr = voc[temp[1]]
                for x,y in arr:
                    gr[x][y]=temp[2]
                if temp[2] in voc:
                    voc[temp[2]]+=voc[temp[1]]
                else:
                    voc[temp[2]]=voc[temp[1]]
                del voc[temp[1]]
                
        elif cc=="MERGE":
            print("2")
        elif cc=="PRINT":
            print("3")
        else:
            answer.append(gr[int(temp[1])][int(temp[2])])
    return answer

print(solution(["UPDATE 1 1 hansik", "UPDATE 1 2 category", 
                "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", 
                "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", 
                "UPDATE 3 2 korean", "UPDATE 3 3 noodle", 
                "UPDATE 3 4 instant", "UPDATE 4 1 pasta", 
                "UPDATE 4 2 italian", "UPDATE 4 3 noodle", 
                "MERGE 1 2 1 3", "MERGE 1 3 1 4", 
                "UPDATE korean hansik",
                "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]	
            ))