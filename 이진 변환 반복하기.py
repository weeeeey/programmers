def change(a, num, cnt):
    if (a == "1"):
        return [cnt, num]
    x = a.replace("0", "")
    charge = num + len(a)-len(x)

    c = str(bin(len(x))[2:])

    return change(c, charge, cnt+1)


def solution(s):
    answer = change(s, 0, 0)
    return answer


print(solution("0111010"))
