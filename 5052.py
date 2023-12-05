def solution(n, arr):
    arr.sort()
    for i in range(1, n):
        if arr[i-1] == arr[i][:len(arr[i-1])]:
            return "NO"
    return "YES"


T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    arr = []
    for _ in range(n):
        a = input().rstrip()
        arr.append(a)

    print(solution(n, arr))
