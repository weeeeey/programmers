from collections import deque


def sol(n, k):
    if not k:
        return "A"*n
    dx = ["A", "B", "C"]
    q = deque()
    q.append((0, 0, 0, 0, 0, []))
    visited = [[[[False]*(451)for _ in range(31)] for _ in range(31)]
               for _ in range(31)]
    visited[0][0][0][0] = True
    while (q):
        sum_k, a, b, c, cur, arr = q.popleft()

        if (sum_k > k):
            continue
        if (cur == n):
            if (sum_k == k):
                return "".join(arr)
            else:
                continue
        for i in range(3):
            nx = dx[i]
            if (i == 0 and visited[a+1][b][c][sum_k] == False):
                visited[a+1][b][c][sum_k] = True
                q.append((sum_k, a+1, b, c, cur+1, arr+[nx]))

            if (i == 1 and visited[a][b+1][c][sum_k+a] == False):
                visited[a][b+1][c][sum_k+a] = True
                q.append((sum_k+a, a, b+1, c, cur+1, arr+[nx]))

            if (i == 2 and visited[a][b][c+1][sum_k+a+b] == False):
                visited[a][b][c+1][sum_k+a+b] = True
                q.append((sum_k+a+b, a, b, c+1, cur+1, arr+[nx]))
    return -1


n, k = map(int, input().rsplit())
print(sol(n, k))
