# dp[i-1] 에 arr에 있는 작대기 한 개 세우기
# dp[i-2] 에 brr에 있는 작대기 한 개 세우기 (1*2를 두개 눕히는 건 합을 구하는 거니까 [i-1]에서 한개 세우는 거랑 중복 됨 )
from collections import deque

# n, a, b = map(int, input().rsplit())
# arr = list(map(int, input().rsplit()))
# brr = list(map(int, input().rsplit()))
# arr.sort()
# brr.sort()


def solution(n, a, b, arr, brr):

    answer = 0
    if (n % 2 == 1):
        answer += arr.pop()
        n -= 1
    for _ in range(0, n, 2):
        one, two = 0, 0
        if (len(arr) >= 2):
            one = arr[-1]+arr[-2]
        if (len(brr) >= 1):
            two = brr[-1]
        if one > two:
            answer += one
            arr.pop()
            arr.pop()
        else:
            answer += two
            brr.pop()
    return answer


# print(solution(n, a, b, arr, brr))
a = set([i for i in range(int(1e5))])
print(a.__sizeof__())
b = set([i for i in range(100)])
print(b.__sizeof__())
