n, m = map(int, input().split())

events = []
for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    events.append((a, -1))
    events.append((b, 1))

dots = list(map(int, input().split()))
for dot in dots:
    events.append((dot, 0))

events.sort()

cnt = 0
ans = {}
for i in range(len(events)):
    if events[i][1] == -1:
        cnt += 1
    elif events[i][1] == 0:
        ans[events[i][0]] = cnt
    elif events[i][1] == 1:
        cnt -= 1

print(*[ans[dot] for dot in dots])

