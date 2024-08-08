n = int(input())
m = int(input())
t = int(input())

l = 0
r = min(m, n) // 2

def rbinsearch(l, r, t):
    s = n * m
    while l != r:
        mid = (l + r + 1) // 2
        s1 = (n - 2 * mid) * (m - 2 * mid)         
        # if s - s1 <= t and n - 2 * mid > 0 and m - 2 * mid > 0:
        if s - s1 <= t:
            l = mid
        else:
            r = mid - 1
    return l
print(rbinsearch(l, r, t))