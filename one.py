from collections import deque
from math import ceil


def solution(time, gold, upgrade):
    answer = 0
    n = len(upgrade)
    q = deque()
    q.append((0, time, 0))

    while (q):
        cur_idx, rest_time, cur_gold = q.popleft()
        if (rest_time <= 0):
            answer = max(answer, cur_gold)
            continue
        if (cur_idx < n-1):
            next_idx = cur_idx+1
            value = cur_gold - upgrade[next_idx][0]
            if (value >= 0):
                q.append((next_idx, rest_time, value))
            else:
                q.append(
                    (cur_idx, rest_time-upgrade[cur_idx][1], cur_gold+gold))
        ttt = ((rest_time)//upgrade[cur_idx][1])*gold
        q.append((cur_idx, 0, ttt+cur_gold))

    return answer


print(solution(
    100,
    200,
    [[0, 5], [1500, 3], [3000, 1]]))
