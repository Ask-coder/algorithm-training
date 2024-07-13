#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
N = int(input())
nums = sorted(list(map(int, input().split())))

K = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(K)]


def bin_search(nums, target):
    res = -1
    if not nums:
        return res

    l = 0
    r = len(nums) - 1
    while l <= r:
        c = (l + r) // 2
        if nums[c] >= target:
            r = c - 1
            res = c
        else:
            l = c + 1

    if l == len(nums):
        return l
    if r == - 1:
        return 0
    return res

ans = []
for interval in intervals:
    l_bound = min(interval)
    r_bound = max(interval)
    l = bin_search(nums, l_bound)
    r = bin_search(nums, r_bound)
    ans.append(str(bin_search(nums, r_bound + 1) - bin_search(nums, l_bound)))

print(' '.join(ans))

