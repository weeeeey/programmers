from collections import deque

n, m = map(int, input().rsplit())

gr = [[]for _ in range(n+1)]
cnt = [0]*(n+1)
answer = []
for _ in range(m):
    small, large = map(int, input().rsplit())
    gr[small].append(large)
    cnt[large] += 1


q = deque()
for i in range(1, n+1):
    if cnt[i] == 0:
        q.append(i)

while (q):
    cur = q.popleft()
    if (cnt[cur] == 0):
        answer.append(cur)
    for next in gr[cur]:
        cnt[next] -= 1
        if (cnt[next] == 0):
            q.append(next)
for a in answer:
    print(a, end=" ")
