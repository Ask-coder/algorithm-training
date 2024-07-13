#! /usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
data = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n):
    tmp = data[i] % 4
    print(tmp)
    if tmp == 1:
        cnt += 1
    elif tmp == 2:
        cnt += 2
    elif tmp == 3:
        cnt += 2
    cnt += data[i] // 4

print(cnt)
