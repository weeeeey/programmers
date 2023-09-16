from collections import deque


def solution(numbers, target):
    answer = 0
    n = len(numbers)

    def repeat(cnt, curr):
        if (curr+1 == n):
            if (cnt == target):
                return 1
            return 0
        a = -1*numbers[curr+1] + cnt
        b = numbers[curr+1] + cnt
        c = repeat(a, curr+1)
        d = repeat(b, curr+1)
        return c+d
    answer = repeat(0, -1)

    return answer


print(solution([1, 1, 1, 1, 1], 3))
