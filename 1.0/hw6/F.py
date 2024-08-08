n, x, y = map(int, input().split())

l = 0
r = n * max(x, y) + 1


while l < r:
    m = (l + r) // 2
    if m // x + m // y >= n - 1 :
        r = m
    else: 
        l = m + 1
print(l + min(x, y))

