#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
n = int(input())
data = list(map(int, input().split()))

res_down = 0
total_down = [0] * n
for i in range(n):
    total_down[i] = abs(data[i] * i - res_down)
    res_down += data[i]

res_up = 0
total_up = [0] * n
for i in range(n - 1, -1, -1):
    total_up[i] = abs(data[i] * (n - i - 1) - res_up)
    res_up += data[i]

print(f"total_down {total_down}")
print(f"total_up {total_up}")
for i in range(n):
    print(total_down[i] + total_up[i], end=' ')

