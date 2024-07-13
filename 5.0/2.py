#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

N = int(input())
l = 0
r = N
res = -1

while l <= r :
    c = (l + r) // 2
    n = N
    k = c
    m = 2
    n -= k
    k -= 1

    while k > 0:
        n -= (k + 1) * m
        if n < 0:
            break
        k -= 1
        m += 1
    if n >= 0:
        l = c + 1
        res = c
    else:
        r = c - 1

print(res)

