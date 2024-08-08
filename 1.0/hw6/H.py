n, k = map(int, input().split())
items = [int(input()) for _ in range(n)]

def rbinsearch(k, items):
    l = 0
    r = max(items)

    while l < r:
        m = (l + r + 1) // 2
        tmp = 0
        for item in items:
            tmp += item // m
        if tmp >= k:
           l = m
        else:
            r = m - 1
    return l

print(rbinsearch(k, items))        