n, r = map(int, input().split())
d = list(map(int, input().split()))

prefix = [0] * n
for i in range(n - 1):
    prefix[i + 1] = d[i + 1] - d[i] + prefix[i]

s = f = 0
cnt = 0
while f < n:
    if prefix[f] - prefix[s] <= r:
        f += 1
    else:
        cnt += n - f
        s += 1

print(cnt)
