def solution(scores):
    n = len(scores)
    wx,wy=scores[0]
    w = wx+wy
    scores.sort(key=lambda x:(-x[0],x[1]))    
    px = scores[0][0]
    py = scores[0][1]
    answer=1
    for i in range(n):
        x,y = scores[i]
        if x>wx and y>wy:
            return -1
        if x+y<=w:
            continue
        if x==px:
            answer+=1
            py = y
        else:
            if py>y:
                continue
            else:
                py = y
                px = x
                answer+=1

            

    return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))

# 어떤 사원이 다른 임의의 사원보다 두 점수 모두 낮으면 인센티브 x
# 그렇지 않은 사원은 두 점수 합이 높은 순으로 인센티브 지급
# 동일 점수일시 그 수만큼 다음 석차는 건너 뜀
# 1등 2명일시, 1등 2명. 3등 1명

# scores 길이는 10만 이하
# [0]은 완호 점수
# 완호가 못 받을 시 -1
# 5 번째 사원은 3 번째 또는 4 번째 사원보다 근무 태도 점수와 동료 평가 점수가 
# 모두 낮기 때문에 인센티브를 받을 수 없습니다.
# 2 번째 사원, 3 번째 사원, 4 번째 사원은 두 점수의 합이 5 점으로 최고점이므로 1 등입니다.
# 1 등이 세 명이므로 2 등과 3 등은 없고 1 번째 사원인 완호는 두 점수의 합이 4 점으로 4 등입니다.

