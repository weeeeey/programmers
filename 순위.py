# result[a,b] : a는 b를 이겼다
def solution(n, results):
    answer = 0  # 정확하게 순위를 매길 수 있는 선수의 수
    gr = [[0]*(n+1) for i in range(n+1)]
    for winner, loser in results:
        gr[winner][loser] = 1

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if gr[i][j] == 0 and gr[i][k] and gr[k][j]:
                    gr[i][j] = 1

    col_sum = [0]*(n+1)
    row_sum = [0]*(n+1)

    for i in range(1, n+1):
        for j in range(1, n+1):
            col_sum[j] += gr[i][j]
            row_sum[i] += gr[i][j]

    print(col_sum)
    print(row_sum)
    for i in range(1, n+1):
        if (col_sum[i]+row_sum[i] == (n-1)):
            answer += 1
    return answer


print(solution(5,	[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
