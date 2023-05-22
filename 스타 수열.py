from itertools import combinations

def solution(a):
    answer = -1
    arr = list(combinations(a,4))
    arr = set(arr)
    print(arr)
    return answer


print(solution([5,2,3,3,5,3]))
# print(solution([1,2,1,3,4,1,1,3]))
# https://yabmoons.tistory.com/610