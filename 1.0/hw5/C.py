n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

m = int(input())
trasses = [tuple(map(int, input().split())) for _ in range(m)]

prefix_LR = [0] * n
prefix_RL = [0] * n
for i in range(1, n):
        prefix_LR[i] = max(prefix_LR[i -1 ] + points[i][1] - points[i - 1][1], prefix_LR[i - 1])
        prefix_RL[-i - 1] = max(prefix_RL[-i] + points[-i - 1][1] - points[-i][1], prefix_RL[-i])

for i in range(m):
    s, f = trasses[i]
    if s <= f:
        res = prefix_LR[f - 1] - prefix_LR[s - 1]

    else:
        res = prefix_RL[f - 1] - prefix_RL[s - 1]
    print(res)

