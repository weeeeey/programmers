def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    m = len(skill_trees)
    a = dict()
    for i in range(n):
        a[skill[i]] = i
    for i in range(m):
        arr = [-1]
        temp = True
        for chr in skill_trees[i]:
            if chr in skill:
                if arr[-1] > a[chr]:
                    temp = False
                    break
                else:
                    arr.append(a[chr])
        if (temp):
            z = True
            for k in range(len(arr)-1):
                if (arr[k]+1 != arr[k+1]):
                    z = False
                    break
            if (z):
                answer += 1

    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
