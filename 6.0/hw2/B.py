n, k = map(int, input().split())
seq = list(map(int, input().split()))

prefix = [0] * (n + 1)

for i in range(n):
    prefix[i + 1] = prefix[i] + seq[i]

print(*prefix)

cnt = 0
for i in range(n):
    l = i
    r = i + 1
    print(f'{l=} {r=}')
    while l < r and r <= n:
        if prefix[r] - prefix[l] == k:
            cnt += 1
            l += 1
            r += 1
            print(l, r, cnt)
        elif prefix[r] - prefix[l] < k:
            print('<')
            r += 1
        else:
            print('>')
            l += 1

print(cnt)



