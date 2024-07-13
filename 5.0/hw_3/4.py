#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
n, k = map(int, input().split())
nums = list(map(int, input().split()))

ans = False
data = dict()
for i, num in enumerate(nums):
    if num not in data:
        data[num] = []
    data[num].append(i)


for key in data:
    if len(data[key]) > 1:
        for i in range(0, len(data[key]) - 1):
            if data[key][i + 1] - data[key][i] <= k:
                ans = True
                break

print('YES' if ans else 'NO')
