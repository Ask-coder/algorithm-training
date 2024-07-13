#! /usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
nums = dict()
for i in map(int, input().split()):
    if i not in nums:
        nums[i] = 0
    nums[i] += 1


val, cnt = 0, 0
freq = {key: 0 for key in nums}
for key in freq:
    freq[key] = nums[key]
    if key + 1 in freq:
        freq[key] += nums[key + 1]
    if freq[key] > cnt:
        cnt = freq[key]
        val = key

res = 0
for key in nums:
    if key - val == 1 or key == val:
        continue
    res += nums[key]

print(res)
