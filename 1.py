def solution(s):
    answer = 0

    for i in range(len(s) - 1):
        if (i % 2 == 0 and s[i] >= s[i + 1]) or (i % 2 == 1 and s[i] <= s[i + 1]):
            answer += 1

    return answer


print(solution([3, -1, 0, 4]))

n = list(map(int, input().rsplit()))

print(n)
