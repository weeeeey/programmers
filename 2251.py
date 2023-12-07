from collections import deque


A, B, C = map(int, input().rsplit())

q = deque()
q.append((0, 0, C))

result = set()
result.add(0)
visited = [[[False]*(C+1) for _ in range(B+1)] for _ in range(A+1)]
visited[0][0][C] = True


while (q):
    a, b, c = q.popleft()
    if (a == 0):
        result.add(c)
    if (a != 0 and a <= b+c):
        print()
    if (b != 0 and b <= a+c):
        print()
    if (c != 0 and c <= a+b):
        if (c == A and visited[c][b][c] == False):
            q.append((c, b, c))
            visited[c][b][c] = True
        if (c == B and visited[a][c][c] == False):
            q.append((a, c, c))
            visited[a][c][c] = True
