from collections import deque
from copy import deepcopy


# 라이언, 어피치
def compare_arr(lion, pitch):
    answer = 0
    for i in range(11):
        if (lion[i] > pitch[i]):
            answer += (10-i)
        else:
            answer -= (10-i)

    return answer


def solution(n, pitch_info):
    max_gap = 0
    answer = []

    q = deque()
    q.append((0, n, [0]*11))
    while (q):
        cur, rest_arrow, lion_info = q.popleft()

        if (rest_arrow < 0):
            continue
        if (rest_arrow == 0):
            apeach, lion = 0, 0
            for i in range(11):
                if not (pitch_info[i] == 0 and lion_info[i] == 0):
                    if pitch_info[i] >= lion_info[i]:
                        apeach += 10 - i
                    else:
                        lion += 10 - i
            if apeach < lion:  # 라이언이 이기면
                gap = lion - apeach
                if max_gap > gap:
                    continue
                if max_gap < gap:
                    max_gap = gap  # 최대점수차 갱신
                    answer = deepcopy(lion_info)
                else:
                    answer = deepcopy(lion_info)  # 최대점수차를 내는 화살상황 저
            continue

        if (cur == 10):
            temp = deepcopy(lion_info)
            temp[10] = rest_arrow
            q.append((-1, 0, temp))
            continue
        temp = deepcopy(lion_info)
        temp[cur] = pitch_info[cur]+1
        q.append((cur+1, rest_arrow-temp[cur], temp))
        q.append((cur+1, rest_arrow, lion_info))

    return answer if len(answer) != 0 else [-1]
# 10점,9잠 --- ,2잠,1점,0점
# k점을 더 많이 맞힌 쪽이 k 점을 가져가는 것
# 둘 다 0이면 0, 같으면 어피치가 k점 가져감
# total_k 가 같으면 어피치 우승


# k번째 화살을 어피치보다 1개 더 쏨. info[k]+1
# k번쨰 화살 안쏘고 아꼈다가 다른 점수에 더 쏨
# 라이언이 어피치를 가장 큰 점수 차로 이기는 방법
# 라이언이 우승 못하면 -1
print(solution(
    5,
    [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))

# [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]
