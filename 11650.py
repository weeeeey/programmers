n = int(input().rstrip())
arr = []
for i in range(n):
    a = list(input().rsplit())
    a += [i]
    arr.append(a)

arr.sort(key=lambda x: (int(x[0]), x[2]))

for a, b, c in arr:
    print(a, b)
