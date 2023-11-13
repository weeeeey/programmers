from collections import deque


A, B, C = map(int, input().rsplit())

q = deque()
q.append((0, 0, C))
result = set()
visited = [[[False]*(201) for _ in range(201)] for _ in range(201)]
visited[0][0][C] = True
while (q):
    a, b, c = q.popleft()
    if (a == 0):
        result.add(c)

    amount = min(a, B-b)
    if not visited[a-amount][b+amount][c]:
        q.append((a-amount, b+amount, c))
        visited[a-amount][b+amount][c] = True

    amount = min(a, C-c)
    if (not visited[a-amount][b][c+amount]):
        q.append((a-amount, b, c+amount))
        visited[a-amount][b][c+amount] = True

    amount = min(b, A-a)
    if (not visited[a+amount][b-amount][c]):
        q.append((a+amount, b-amount, c))
        visited[a+amount][b-amount][c] = True

    amount = min(b, C-c)
    if (not visited[a][b-amount][c+amount]):
        q.append((a, b-amount, c+amount))
        visited[a][b-amount][c+amount] = True

    amount = min(c, A-a)
    if (not visited[a+amount][b][c-amount]):
        q.append((a+amount, b, c-amount))
        visited[a+amount][b][c-amount] = True

    amount = min(c, B-b)
    if (not visited[a][b+amount][c-amount]):
        q.append((a, b+amount, c-amount))
        visited[a][b+amount][c-amount] = True


print(sorted(list(result)))
