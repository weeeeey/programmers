from math import ceil


def solution(n, words):
    answer = []
    m = len(words)
    temp = -1
    a = [words[0]]
    for i in range(m-1):
        if words[i][-1] != words[i+1][0]:
            temp = i+2
            break
        if words[i+1] in a:
            temp = i+2
            break
        a.append(words[i])
    print(a)

    if (temp == -1):
        answer = [0, 0]
    else:
        c = temp % n if temp % n != 0 else n
        d = ceil(temp/n)
        answer = [c, d]

    return answer


# 번호, 차례
# 탈락자 x면 [0,0]
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))
