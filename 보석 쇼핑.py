def solution(gems):
    answer = []
    n = len(gems)
    s = list(set(gems))
    z = [s.index(i) for i in gems]
    print(z)
    
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))