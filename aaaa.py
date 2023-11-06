from collections import deque

answer = 1000

a = "...#....."

q = deque()
n = len(a)
dp = [100]*103
for i in range(len(a)):
    if a[i] == ".":
        q.append((i, 1))
        dp[i] = 1
        break

while (q):
    idx, cnt = q.popleft()
    if (idx >= n):
        answer = min(answer, cnt)
        continue
