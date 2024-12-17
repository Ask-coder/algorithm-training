MIDNIGHT = 60 * 24

n = int(input())
data = []


for _ in range(n):
    h1, m1, h2, m2 = map(int, input().split())
    data.append((h1 * 60 + m1, h2 * 60 + m2))

events = []
for i in range(n):
    events.append((data[i][0], 1, i))
    events.append((data[i][1], -1, i))

events.sort()
opened = set()
time_start = 0
res = 0

# первый проход
for i in range(len(events)):
    if events[i][1] == -1:
        if events[i][2] in opened:
            if len(opened) == n:
                res += abs(events[i][0] - time_start)
            opened.remove(events[i][2])
    elif events[i][1] == 1:
        opened.add(events[i][2])
        if len(opened) == n:
            time_start = events[i][0]

time_start = 0
if opened:
    new_opened = opened.copy()
    for i in range(len(events)):
        if events[i][1] == -1:
            if len(new_opened) == n:
                res += abs(events[i][0] - time_start)
            
            if events[i][2] in opened:
                opened.remove(events[i][2])
            new_opened.remove(events[i][2])
            if not opened:
                break
        elif events[i][1] == 1:
            new_opened.add(events[i][2])
            if len(new_opened) == n:
                time_start = events[i][0]


print(res)



