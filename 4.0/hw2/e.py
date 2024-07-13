#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

def countpalindromes(ss):
    s = "$#" + "#".join(ss)+"#"
    n = len(s)
    p = [0] * n
    l = 0
    r = -1
    for i in range(n):
        k = 1 if i > r else min (p[l+r-i], r-i+1)
        while (i+k < n and i-k >= 0 and s[i+k] == s[i-k]):
            k += 1
        p[i] = k
        if (i+k-1 > r):
            l = i-k+1
            r = i+k-1
    return(sum([x//2 for x in p]))


if __name__ == '__main__':
    print(countpalindromes(input()))
# s = '#' + '#'.join(input()) + '#'
# n = len(s)
# x_ = 257
# p = 10 ** 9 + 7
# h = [0] * (n + 1)
# h_r = [0] * (n + 1)
# x = [0] * (n + 1)
# x[0] = 1
# print(s)
# for i in range(1, n + 1):
#     h[i] = (h[i - 1] * x_ + ord(s[i // 2 - 1])) % p
#     h_r[i] = (h_r[i - 1] * x_ + ord(s[-i // 2])) % p
#     x[i] = (x[i - 1] * x_) % p
#


