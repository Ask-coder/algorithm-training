n, k = map(int, input().split())
mapper = {}

for _ in range(k):
    line = input()
    ts, token = line.split()
    if token not in mapper:
        mapper[token] = set()

    if len(mapper[token]) <= n:
        mapper[token].add(int(ts))
        print(line)
    else:
        tmp = max(min(mapper[token]), int(ts) - 1000)
        if tmp <= 1000:
            print(line)
        mapper[token].remove(min(mapper[token]))
        mapper[token].add(int(ts))
