n = int(input().rstrip())
arr = []
for i in range(n):
    arr.append([int(input().rstrip())]+[i])

brr = sorted(arr, key=lambda x: x[0])
temp = [0]*n


for i in range(n):
    temp[i] = brr[i][1]-i
print(max(temp)+1)
