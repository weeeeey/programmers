from collections import deque


def solution(a, b, c, d):
    q = deque([(0, 0, 0)])
    v = set([(0, 0, 0)])
    cnt = 0

    while q:
        for _ in range(len(q)):
            x, y, z = q.popleft()

            if x == d or y == d or z == d:
                return cnt

            states = [
                (a, y, z), (x, b, z), (x, y, c),
                (0, y, z), (x, 0, z), (x, y, 0),
                (max(x - (b - y), 0), min(x + y, b), z),
                (max(x - (c - z), 0), y, min(x + z, c)),
                (min(x + y, a), max(y - (a - x), 0), z),
                (x, max(y - (c - z), 0), min(y + z, c)),
                (min(x + z, a), y, max(z - (a - x), 0)),
                (x, min(y + z, b), max(z - (b - y), 0))
            ]

            for state in states:
                if state not in v:
                    v.add(state)
                    q.append(state)

        cnt += 1

    return -1


print(solution(3, 5, 7, 1))
print(solution(3, 6, 9, 4))
