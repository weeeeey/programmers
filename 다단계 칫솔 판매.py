# 판매원들의 각각의 이익금을 enroll 이름이 포함된 순서에 따라 출력

            # 판매원 이름,   추천인, 물건 판 판매원 이름, 그 판매원들의 이익
def solution(   en,     ref,    sel,            amount):
    n = len(en)
    answer = [0]*n
    tree = dict()
    profit = dict()
    profit["center"] = 0
    tree["center"]="center"
    for i in range(n):
        profit[en[i]]=0
        if ref[i]=='-':
            tree[en[i]]='center'
        else:
            tree[en[i]]=ref[i]
    for i in range(len(sel)):
        name = sel[i]
        parent = tree[name]
        money = amount[i]*100
        profit[name]+=int(money*0.9)
        profit[parent]+=int(money*0.1)
        money = int(money*0.01)
        while(True):
            profit[parent]-=money
            parent=tree[parent]
            profit[parent]+=money
            money=int(money*0.1)
            if(money<0 or parent=="center"):
                break
    for i in range(n):
        answer[i]=profit[en[i]]
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                ["-",     "-",   "mary", "edward", "mary", "mary", "jaimie", "edward"],
                ["young", "john", "tod", "emily", "mary"],
                [12, 4, 2, 5, 10]))

["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
[360,     958,      108,     0,     450,     18,      180,   1080]
