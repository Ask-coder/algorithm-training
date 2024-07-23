n, m, k = map(int, input().split())
mines = {(tuple(map(int, input().split()))) for _ in range(k)}
seek = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

ans = []
for i in range(n):
    row = []
    for j in range(m):
        char = ''        
        if (i + 1, j + 1) in mines:
            char = '*'
        else:
            cnt = 0
            for item in seek:
                if (i + 1 + item[0], j + 1 + item[1]) in mines:
                    cnt += 1
            char = str(cnt)
        row.append(char)

    ans.append(row)

for item in ans:
    print(' '.join(item))