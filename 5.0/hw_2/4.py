#! /usr/bin/env python3
# -*- coding: utf-8 -*-

offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]
N = int(input())
data = set(tuple(map(int, (input().split()))) for _ in range(N))

ans = 0
for item in data:
    ans += 4
    for i in offset:
        if (item[0] + i[0], item[1] + i[1]) in data:
            ans -= 1

print(ans)
