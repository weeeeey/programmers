def solution(nodeinfo):
    n = len(nodeinfo)
    for i in range(n):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x: (-x[1], x[0]))
    level = nodeinfo[0][1]
    gr = [[] for i in range(level+1)]
    gr[level].append(nodeinfo[0])
    for i in range(1, n):
        x, y, node = i

    # start = 0


print(solution([[5, 3], [11, 5], [13, 3], [3, 5],
      [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]))
