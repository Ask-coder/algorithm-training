n, m = map(int, input().split())

events = []
cnt = 0
for i in range(m):
    b, e = map(int, input().split())
    events.append((b, -1))
    events.append((e, 1))

events.sort()
cnt = 0
res = 0
idx = 0
for i in range(len(events)):
    if cnt == 0:
        res += events[i][0] - idx
    
    if events[i][1] == -1:
        cnt += 1

    elif events[i][1] == 1:
        cnt -= 1

    if cnt == 0:
        idx = events[i][0] + 1

res += n - idx

print(res)