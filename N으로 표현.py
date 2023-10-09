from collections import deque

# 붙, 덧, 뺄, 곱, 나


def solution(n, ans):
    if (n == ans):
        return 1
    q = deque()
    q.append([1, [n]])
    while (q):
        step, query = q.popleft()
        if (step > 8):
            continue

    return -1


print(solution(5, 12), "답은 4가 나와야 함")
print(solution(2, 11), "답은 3이 나와야 함")

# arr = [5, 5]
# print("".join(map(str, arr)))

# 나누기에서 나머지 무시
# 최솟값 8보다 크면 -1

# number가 나오면 멈추기
'''
1 : 5 
2 : 55, 5+5, 5-5 , 5*5, 5//5 
3 : 555, 55+5 ,55-5, 55*5, 55//5 
    5+55, 5+5+5, 5+5-5, 5+5*5, 5+5//5
    5-55, 5-5+5, 5-5-5, 5-5*5, 5-5//5
    5*55, 5*5+5, 5*5-5, 5*5*5, 5*5//5
    5//55, 5//5+5, 5//5-5, 5//5*5, 5//5//5 

'''
