#! /usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
data = list(map(int, input().split()))
res = [''] * (n - 1)
first_odd = -1
count_odd = data[0] % 2
for i in range(n-1):
    if (data[i] + data[i + 1]) == 0:
        res[i] = chr(120)
    else:
        res[i] = chr(43)
        if data[i + 1] % 2:
            count_odd += 1
    if first_odd == -1 and data[i] % 2:
        first_odd = i

if count_odd % 2:
    print(''.join(res))
else:
    res[first_odd] = chr(120) if res[first_odd] == chr(43) else chr(43)
    print(''.join(res))
