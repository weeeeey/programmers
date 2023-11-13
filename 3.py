def solution(n):
    eggs = [0]
    dragons = []
    for day in range(1, n + 1):

        eggs_to_hatch = [egg for egg in eggs if egg + 2 == day]
        for _ in eggs_to_hatch:
            dragons.append(0)
        eggs = [egg for egg in eggs if egg + 2 != day]

        for i in range(len(dragons)):
            if dragons[i] < 4:
                dragons[i] += 1
                eggs.append(day)

    return len(dragons) + len([egg for egg in eggs if egg + 2 >= n])


print(solution(6))
