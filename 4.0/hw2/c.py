#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#


def z_func(s):
    z = [0] * len(s)
    l, r = 0, 0
    for i in range(1, len(s)):
        z[i] = max(0, min(z[i - l], r - i))
        while i + z[i] < len(s) and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l, r = i , i + z[i]
    return z


if __name__ == "__main__":
    print(' '.join(list(map(str, z_func(input())))))


