#! /usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
data_a = []
data_b = []
max_neg_a = (None, -1) # максимум среди отрицательного подъёма
max_pos_b = (None, -1) # максимум среди положительного подъёма
pos = []
neg = []
cur = max_h = 0

for i in range(N):
    a, b = map(int, input().split())
    data_a.append(a)
    data_b.append(b)
    diff = a - b
    if diff <= 0:
        neg.append(i)
        if max_neg_a[0] == None:
            max_neg_a = (a, i)
        else:
            max_neg_a = max(max_neg_a, (a, i))
    else:
        pos.append(i)
        if max_pos_b[0] == None:
            max_pos_b = (b, i)
        else:
            max_pos_b = max(max_pos_b, (b,i))

for i in pos:
    if i != max_pos_b[1]:
        max_h = max(max_h, cur + data_a[i])
        cur += data_a[i] - data_b[i]

if pos:
    max_h = max(max_h, cur + data_a[max_pos_b[1]])
    cur += data_a[max_pos_b[1]] - data_b[max_pos_b[1]]
if neg:
    max_h = max(max_h, cur + data_a[max_neg_a[1]])


print(max_h)
ans = []
if pos:
    for i in pos:
        if i != max_pos_b[1]:
            ans.append(str(i + 1))
    ans.append(str(max_pos_b[1] + 1))

if neg:
    ans.append(str(max_neg_a[1] + 1))

    for i in neg:
        if i != max_neg_a[1]:
            ans.append(str(i + 1))

print(' '.join(ans))
