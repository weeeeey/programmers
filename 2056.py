from collections import deque

answer = 0
n = int(input().rstrip())
gr = [[]for _ in range(n+1)]
time = [0]*(n+1)
answer = [0]*(n+1)
q = deque()
for i in range(1, n+1):
    temp = list(map(int, input().rsplit()))
    a, b, c = temp[0], temp[1], temp[2:]
    time[i] = a
    for d in c:
        gr[d].append(i)
    if not b:
        q.append(i)
        answer[i] = a

while (q):
    cur = q.popleft()
    for next in gr[cur]:
        if (answer[next] < answer[cur]+time[next]):
            answer[next] = answer[cur]+time[next]
            q.append(next)
print(max(answer))
