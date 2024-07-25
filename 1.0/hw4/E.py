n = int(input())
my_max = 1
data = {}
for _ in range(n):
    w, h = map(int, input().split())
    if w > my_max:
        my_max = w
    if w not in data:
        data[w] = []
    data[w].append(h)

ans = 0
keys = sorted(data, reverse=True)
for key in keys:
    ans += max(data[key])

print(ans)