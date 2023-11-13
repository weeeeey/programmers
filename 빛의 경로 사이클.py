from collections import deque


def move(d, n, m, grid):
    dz = ["상", "우", "하", "좌"]
    dx = [-1, 0, 1, 0]  # 12,3,6,9 시계 방향
    dy = [0, 1, 0, -1]
    # L이면 0->3, 1->0, 2->1, 3->2  0===3, else -1씩 하기
    # R이면 0->1, 1->2, 2=>3, 3->0  3===0, else +1
    q = deque()
    q.append((0, 0, d, 0))
    visited = [[[-1]*4 for _ in range(m)] for _ in range(n)]

    while (q):
        x, y, dir, cnt = q.popleft()
        if ([x, y] == [0, 0] and dir == d and visited[x][y][dir] != -1):
            return visited[x][y][dir]

        nx = (x + dx[dir]) % n
        ny = (y + dy[dir]) % m

        if visited[nx][ny][dir] != -1:
            continue

        nextDir = dir
        if grid[nx][ny] == "L":
            nextDir = dir-1 if dir != 0 else 3

        if grid[nx][ny] == "R":
            nextDir = dir + 1 if dir != 3 else 0

        visited[nx][ny][dir] = cnt+1
        q.append((nx, ny, nextDir, cnt+1))


def solution(grid):
    answer = []
    n = len(grid)
    m = len(grid[0])

    for i in range(4):
        aa = move(i, n, m, grid)
        if (aa):
            answer.append(aa)
    return answer


a = ["S"]
print(solution(a))
# 좌 우 상 하
# [-1 -1 -1 -1]  [-1 -1 -1 -1]
#     직          왼

# [-1 -1 -1 -1]  [-1 -1 -1 -1]
#     왼          오
