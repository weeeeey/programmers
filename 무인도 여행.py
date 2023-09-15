from collections import deque


def solution(maps):
    answer = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for i in range(n)]
    for i in range(n):
        for j in range(m):
            if (maps[i][j] == "X" or visited[i][j] == True):
                continue
            else:
                q = deque()
                q.append((i, j))
                s = int(maps[i][j])
                visited[i][j] = True
                while (q):
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if nx < 0 or nx >= n or ny < 0 or ny >= m:
                            continue
                        if visited[nx][ny] == True:
                            continue
                        if maps[nx][ny] == "X":
                            continue
                        visited[nx][ny] = True
                        s += int(maps[nx][ny])
                        q.append((nx, ny))
                answer.append(s)
    answer.sort()

    return answer if len(answer) != 0 else [-1]


print(solution(["X591X", "X1X5X", "X231X", "1XXX1"]))
