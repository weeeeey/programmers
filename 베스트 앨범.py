def solution(gens, plays):
    answer = []
    s = list(set(gens))
    n = len(s)
    m=len(gens)
    gens=["a"]+gens
    plays=[-1]+plays
    g = [[0,0,0] for i in range(n+1)] 
    for i in range(1,m+1):
        idx = s.index(gens[i])
        a,b= g[idx][1:]
        play = plays[i]
        A,B = plays[a],plays[b]

        g[idx][0]+=play
        if play<=B:
            continue
        elif play==A:
            g[idx][1:]=[a,i]
        elif play>A:
            g[idx][1:]=[i,a]
        else:
            g[idx][1:]=[a,i]
    g.sort(key=lambda x:-x[0])
        
    for i in range(n+1):
        a, b = g[i][1]-1,g[i][2]-1
        if a!=-1:
            answer.append(a)
        if b!=-1:
            answer.append(b)

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))