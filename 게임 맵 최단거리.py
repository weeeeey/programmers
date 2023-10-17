from collections import deque


def solution(maps):
    answer = 0
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n = len(maps)
    m = len(maps[0])
    q = deque()
    q.append((0, 0))
    visited = [[0]*m for i in range(n)]
    while (q):
        x, y = q.popleft()
        if ([x, y] == [n-1, m-1]):
            return visited[x][y]
        for i in range(4):
            nx = x + dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] != 0:
                continue
            if maps[nx][ny] == 0:
                continue
            visited[nx][ny] = visited[x][y]+1
            q.append((nx, ny))

    return -1
