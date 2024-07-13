#! /usr/bin/env python3
# -*- coding: utf-8 -*-


line_1 = input()
line_2 = input()

res_1 = dict()
res_2 = dict()

for i in line_1:
    if i not in res_1:
        res_1[i] = 0
    res_1[i] += 1


for i in line_2:
    if i not in res_2:
        res_2[i] = 0
    res_2[i] += 1

print( 'YES' if res_1 == res_2 else 'NO')
