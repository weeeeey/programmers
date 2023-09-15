def solution(brown, yellow):
    answer = []
    s = brown+yellow
    a = int((s)**(1/2))
    for i in range(a, s):
        if not s % i:
            j = s//i
            if ((i-2)*(j-2) == yellow):
                answer = [i, j]
                break

    if answer[0] < answer[1]:
        answer[0], answer[1] = answer[1], answer[0]
    return answer


print(solution(24, 24))
