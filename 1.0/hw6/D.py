n, a, b, w, h = map(int, input().split())
   

def rbinsearch(n, a, b, w, h):
    l = 0
    r = max(w, h) // 2 + 1
    while l != r:
        m = (l + r + 1) // 2
        if (w // (a + 2 * m)) * (h // (b + 2 * m)) >= n or (w // (b + 2 * m)) * (h // (a + 2 * m)) >= n:
            l = m
        else:
            r = m - 1
    return l

print(rbinsearch(n, a, b, w, h))