#! /usr/bin/env python3
# -*- coding: utf-8 -*-

L, x1, v1, x2, v2 = map(int, input().split())

COUNT = 100
i = 1
samples = []
if x1 == x2 or x1 == L - x2:
    samples.append(0.0)

while i < COUNT:
    j = 1
    while j < COUNT:
        t1 = -1
        t2 = -1

        if v2 != v1:
            t1 = ((x2 - x1) + L *(i - j)) / (v1 - v2)
            if t1 > 0:
                samples.append(t1)
        if v1 != -v2:
            t2 = (L * (i - j) + L - x1 - x2) / (v1 + v2)
            if t2 > 0:
                samples.append(t2)
        j += 1
    i += 1

if samples:
    print('YES')
    print(min(samples))
else:
    print('NO')



