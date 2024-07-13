arr = list(map(int, input().split()))

res = True
for i in range(1, len(arr)):
    if arr[i - 1] >= arr[i]:
        res = False

print('YES' if res else 'NO')