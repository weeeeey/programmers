# dp[i-1] 에 arr에 있는 작대기 한 개 세우기
# dp[i-2] 에 brr에 있는 작대기 한 개 세우기 (1*2를 두개 눕히는 건 합을 구하는 거니까 [i-1]에서 한개 세우는 거랑 중복 됨 )
from copy import deepcopy


def sol(n, arr, brr, aCnt, bCnt):
    answer = 0

    return answer


n, a, b = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))
arr.sort(reverse=True)
brr.sort(reverse=True)

if (n == 1):
    print(arr[0])
elif (n == 2):
    c = 0
    if a >= 2:
        c = arr[0]+arr[1]
        print(max(c, brr[0]))
else:
    print(sol(n, arr, brr, a, b))
