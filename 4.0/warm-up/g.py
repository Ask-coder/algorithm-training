#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
n, m = map(int, input().split())
data = [[0] * (m + 1)]
for _ in range(n):
    data.append([0] + list(map(int, input().split())))
my_max = 0

F = data.copy()

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if data[i][j] != 0:
            F[i][j] = min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1]) + 1
            my_max = max(F[i][j], my_max)

print(my_max)


