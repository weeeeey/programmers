import heapq


def solution(n, route):
    answer = 0

    gr = [[] for i in range(n+1)]
    for i in route:
        s, d, w = i
        gr[s].append([d, w])
        gr[d].append([s, w])
    dict = [-1]*(n+1)
    dict[1] = 0
    q = []
    for i in gr[1]:
        d, w = i
        dict[d] = w
        heapq.heappush(q, (w, d))
    while (q):
        drunk, cur = heapq.heappop(q)
        if (n == cur):
            answer = drunk
            break
        for next in gr[cur]:
            next_num, next_w = next
            d = max(drunk, next_w)
            if (dict[next_num] == -1):
                dict[next_num] = d
                heapq.heappush(q, (d, next_num))
                continue
            if (d >= dict[next_num]):
                continue
            dict[next_num] = d
            heapq.heappush(q, (d, next_num))

    return answer


print(solution(5, [[5, 1, 15], [4, 2, 6], [1, 4, 8], [
      3, 2, 10], [1, 2, 7], [5, 4, 6], [2, 5, 5]]))
