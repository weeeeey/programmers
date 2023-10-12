def str_to_int(str):
    pt = str.split(":")
    return int(pt[0])*3600 + int(pt[1])*60 + int(pt[2])


def int_to_str(int):
    h = int//3600
    h = str(h) if h >= 10 else "0"+str(h)
    int %= 3600
    m = int//60
    m = str(m) if m >= 10 else "0"+str(m)
    s = int % 60
    s = str(s) if s >= 10 else "0"+str(s)
    return h+":"+m+":"+s


def solution(ptt, adtt, logs):
    answer = [0, 0]
    pl = len(logs)
    pt = str_to_int(ptt)
    adt = str_to_int(adtt)

    dp = [0]*(pt+1)

    for i in range(pl):
        a, b = logs[i].split("-")
        start = str_to_int(a)
        end = str_to_int(b)
        dp[start] += 1
        dp[end] -= 1

    for i in range(1, pt+1):
        dp[i] = dp[i-1] + dp[i]

    state = 0
    s, e = 0, -1
    while (s <= pt and e <= pt):
        while (e+1 <= pt and e+1-s < adt):
            e += 1
            state += dp[e]
            if (state > answer[1]):
                answer[0] = s
                answer[1] = state
        state -= dp[s]
        s += 1

    return int_to_str(answer[0])


print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14",
                                        "00:40:31-01:00:00",
                                        "00:25:50-00:48:29",
                                        "01:30:59-01:53:29",
                                        "01:37:44-02:02:30"]))
