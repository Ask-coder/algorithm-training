#! /usr/bin/env python3
# -*- coding: utf-8 -*-


a = int(input())
b = int(input())
n = int(input())

print("Yes" if a > (b + n - 1) // n else "No")
