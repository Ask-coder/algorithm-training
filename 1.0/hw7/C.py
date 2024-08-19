n, d = map(int, input().split())
x = list(map(int, input().split()))

events = []
for xi in x:
    events.append((xi, -1))
    events.append((xi + d, 1))

events.sort()
cnt = 0
num_var = 1
ans_cnt = 0
variants = {}
for i in range(len(events)):
    if events[i][1] == -1:
        cnt += 1
        ans_cnt = max(cnt, ans_cnt)
    elif events[i][1] == 1:
        cnt -= 1

for i in range(len(events)):
    if events[i][1] == -1:
        variants[events[i][0]] = num_var
        if num_var < ans_cnt:
            num_var += 1
        else:
            num_var = 1

print(ans_cnt)
print(*[variants[xi] for xi in x])
