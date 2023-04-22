def solution(n, times):
    answer = 0
    end = n*max(times)
    start = 0
    while(start<=end):
        mid = (start+end)//2
        s=0
        for t in times:
            s+=mid//t
            if s>=n:
                break
        if s>=n:
            end = mid-1
        else:
            start=mid+1

    return start

print(solution(6,[7, 10]))

