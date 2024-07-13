#! /usr/bin/env python3
# -*- coding: utf-8
#
my_dict = set(input().split())
data = input().split()

ans = []
for item in data:
    r = 1
    res = ''
    while r < len(item):
        if item[:r] in my_dict:
            res = item[:r]
            break
        r += 1
    ans.append(res if res else item)

print(' '.join(ans))
