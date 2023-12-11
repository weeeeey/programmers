from collections import deque

answer = 0
n = int(input().rstrip())
cnt = [0]*(n+1)
gr = [[]for _ in range(n+1)]
time = [0]*(n+1)

for i in range(1, n+1):
    temp = list(map(int, input().rsplit()))
    t, b = temp[0], temp[1]
    time[i] = t
    c = temp[2:]
    for k in c:
        cnt[i] += 1
        gr[k].append(i)


q = deque()
visited_time = [0]*(n+1)
for i in range(1, n+1):
    if (cnt[i] == 0):
        q.append(i)
        visited_time[i] = time[i]

while (q):
    cur, cur_t = q.popleft()
    temp = []
    for next in gr[cur]:
        cnt[next] -= 1
        if (cnt[next] == 0):
            temp.append(next)
