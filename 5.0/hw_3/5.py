#! /usr/bin/env python3
# -*- coding: utf-8 -*-


n, nums_1 = int(input()), set(map(int, input().split()))
n, nums_2 = int(input()), set(map(int, input().split()))
n, nums_3 = int(input()), set(map(int, input().split()))

res = set()
for i in nums_2:
    if i in nums_1:
        res.add(i)

for i in nums_3:
    if i in nums_1 or i in nums_2:
        res.add(i)

print(' '.join([str(i) for i in sorted(res)]))
