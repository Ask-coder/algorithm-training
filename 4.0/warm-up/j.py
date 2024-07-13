#! /usr/bin/env python3
# -*- coding: utf-8 -*-

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    groups = n // a
    tmp = n % a
    print("YES" if n % a <= groups * (b -a) else "NO")

