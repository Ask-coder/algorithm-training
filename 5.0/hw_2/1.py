#! /usr/bin/env python3
# -*- coding: utf-8 -*-

k = int(input())
data = [tuple(map(int, input().split())) for _ in range(k)]

min_x = max_x = data[0][0]
min_y = max_y = data[0][1]
for i in range(1, k):
    min_x = min(min_x, data[i][0])
    max_x = max(max_x, data[i][0])
    min_y = min(min_y, data[i][1])
    max_y = max(max_y, data[i][1])

print(min_x, min_y, max_x, max_y)

