a = int(input())
b = int(input())
c = int(input())
d = int(input())

def func(a, b, c, d):
    ans = []

    if a == 0 or b == 0:
        if a == 0:
            ans.append((1, c + 1))
        if b == 0:
            ans.append((1, d + 1))
    if c == 0 or d == 0:
        if c == 0:
            ans.append((a + 1, 1))
        if d == 0:
            ans.append((b + 1, 1))  

    if a > 0 and c > 0 and c != 0 and d != 0:
        ans.append((b + 1, d + 1))
    if b > 0 and d > 0 and a != 0 and c != 0:
        ans.append((a + 1, c + 1))
    if a > 0 and b > 0:
        ans.append((max(a, b) + 1, 1))
    if c > 0 and d > 0:
        ans.append((1, max(c, d) + 1))

    return min(ans, key=sum)

print(*func(a, b, c, d))

# print(func(6, 2, 7, 3) == (3, 4))
print(func(0, 5, 1, 2))
