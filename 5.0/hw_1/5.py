#! /usr/bin/env python3
# -*- coding: utf-8 -*-


n, k, d = map(int, input().split())

res = ''
tmp = -1
for i in range(10):
    if not (n * 10 + i) % k:
        tmp = i
        break


print(str(n * 10 + tmp) + '0' * (d - 1) if tmp != -1 else -1)


