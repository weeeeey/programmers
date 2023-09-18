from math import floor


def findPoint(arr, brr):
    a1, b1, c1 = arr
    a2, b2, c2 = brr

    if (a1*b2 == a2*b1):
        return False
    x = (b1*c2-c1*b2)/(a1*b2-b1*a2)
    y = (c1*a2-a1*c2)/(a1*b2-b1*a2)

    xx = floor(x)
    yy = floor(y)
    if (xx == x and yy == y):
        return [xx, yy]
    else:
        return False


def solution(line):
    answer = []
    n = len(line)
    for i in range(n-1):
        for j in range(i, n):
            temp = findPoint(line[i], line[j])
            if (temp):
                answer.append(temp)

    gr = []
    # print(answer)
    w1, w2 = min(answer, key=lambda x: x[0])[0], max(
        answer, key=lambda x: x[0])[0] + 1
    h1, h2 = min(answer, key=lambda x: x[1])[1], max(
        answer, key=lambda x: x[1])[1] + 1

    # 별을 포함하는 최소한의 크기 배열 생성
    gr = [['.'] * (w2 - w1) for _ in range((h2 - h1))]

    # 그림의 시작점을 기준으로 교점 위치 "*" 변환
    for x, y in answer:
        gr[y-h1][x-w1] = '*'

    gr.reverse()

    return [''.join(a) for a in gr]

# "....*....4"

# ".........3"

# ".........2"

# "*.......*1"

# ".........0"

# ".........-1"


# ".........-2"
# ".........-3"
# "*.......*-4"
print(solution([[2, -1, 4], [-2, -1, 4],
      [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# print(findPoint([2, -1, 4], [0, -1, 1]))
