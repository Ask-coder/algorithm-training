a = int(input())
b = int(input())
c = int(input())

def lbinsearch(a, b, c):
    l = 0
    r = (a + b + c) * 2
    n = a + b + c
    sm = 2 * a + 3 * b + 4 * c

    while l < r:
        m = (l + r) // 2
        if 2 * (sm + m * 5) >= 7 * (n + m):
            r = m 
        else: 
            l = m + 1
    return l

print(lbinsearch(a, b, c))