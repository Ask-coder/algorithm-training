n, k = map(int, input().split())
trees = list(map(int, input().split()))

l = 0
res = []
tmp = {}

for i in range(n):
    if trees[i] not in tmp:
        tmp[trees[i]] = 0
    tmp[trees[i]] += 1

    while tmp[trees[l]] > 1:
        tmp[trees[l]] -= 1
        l += 1

    if len(tmp) == k:
        res.append((l + 1, i + 1))

print(*min(res, key=lambda x: x[1] - x[0]))

