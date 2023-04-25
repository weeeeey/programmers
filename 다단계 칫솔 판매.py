# 판매원들의 각각의 이익금을 enroll 이름이 포함된 순서에 따라 출력

            # 판매원 이름,   추천인, 물건 판 판매원 이름, 그 판매원들의 이익
def solution(   en,     ref,    sel,            amount):
    n = len(en)
    answer = [0]*n
    tree = dict()
    empty = []
    profit = dict()
    for i in range(n):
        profit[en[i]]=0
        if ref[i]=='-':
            continue
        tree[en[i]]=ref[i]
    

    for i in range(len(sel)):
        name = sel[i]
        a = amount[i]*100
        sell,ps = a*0.9, a*0.1
        profit[name]+=int(sell)
        p = name
        while(p in tree):
            profit[tree[p]]+=int(ps)
            break    
    print(profit)
    # return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                ["-",     "-",   "mary", "edward", "mary", "mary", "jaimie", "edward"],
                ["young", "john", "tod", "emily", "mary"],
                [12, 4, 2, 5, 10]))

