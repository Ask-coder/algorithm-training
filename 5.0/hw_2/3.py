#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
N = int(input())
data = list(map(int, input().split()))

my_sum = 0
my_max = data[0]
for item in data:
    my_max = max(my_max, item)
    my_sum += item

my_sum -= my_max
print(my_max - my_sum if my_max > my_sum else my_max + my_sum)
