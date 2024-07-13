#! /usr/bin/env python3
# -*- codign: utf-8 -*-


def prefix_func(s):
    p = [0] * len(s)
    k = 0

    for i in range(1, len(s)):
        k = p[i - 1]
        while k > 0 and s[i] != s[k]:
            k = p[k - 1]
        if s[i] == s[k]:
            k += 1
        p[i] = k

    return p


if __name__ == "__main__":
    s = input()
    print(len(s) - max(prefix_func(s)))
