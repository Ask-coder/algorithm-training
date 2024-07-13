#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
def is_equal(from_1: int, from_2: int, slen: int)-> bool:
    return (
        (h[from_1 + slen] + h[from_2] * x[slen]) % p ==
        (h[from_2 + slen] + h[from_1] * x[slen]) % p
    )


if __name__ == "__main__":
    s = input()
    Q = int(input())
    # x_ = 257
    x_ = 10
    p = 10 ** 9 + 7
    n = len(s)

    x = [0] * (n + 1)
    h = [0] * (n + 1)
    x[0] = 1
    s = ' ' + s

    for i in range(1, n + 1):
        h[i] = (h[i - 1] * x_ + ord(s[i])) % p
        x[i] = (x[i - 1] * x_) % p

    for _ in range(Q):
        l, a, b = map(int, input().split())
        print("yes" if is_equal(a, b, l) else "no")


