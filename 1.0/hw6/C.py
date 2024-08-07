w, h, n = map(int, input().split())


max_side = max(w, h) * n

l = 0
r = max_side

while l < r:
    m = (l + r) // 2
    if (m // w) * (m // h) >= n:
        r = m
    else:
        l = m + 1

print(l) 