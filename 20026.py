dp = [[0]*10 for _ in range(10)]


def blue_drop(t, x, y):
    print(x, y)


def green_drop(t, x, y):
    print(x, y)


def solution(n, info):
    answer = 0
    special_area = [4, 5]
    color_area = [6, 7, 8, 9]
    for t, x, y in info:
        blue_drop(t, x, y)
        green_drop(t, x, y)

    return answer


n = int(input().rstrip())
info = []
for i in range(n):
    info.append(list(map(int, input().rsplit())))

print(solution(n, info))
