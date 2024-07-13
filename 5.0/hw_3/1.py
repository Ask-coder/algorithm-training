#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
n = int(input())
_, res = input(), set(input().split())


for item in range(1, n):
    _ = input()
    res = res.intersection(set(input().split()))

print(len(res))
print(' '.join(sorted(res)))

