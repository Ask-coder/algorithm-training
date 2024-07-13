#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
n = int(input())
data = list(map(int, input().split()))
res = ''
first_odd = -1
count_odd = data[0] % 2
tmp = data[0]

for i in range(1, n):
    if not (tmp + data[i]) % 2:
        res += chr(120)
    else:
        res += chr(43)
        if data[i] % 2:
            count_odd += 1

    if first_odd == - 1 and tmp % 2:
        first_odd =  i - 1
    tmp = data[i]

if count_odd % 2:
    print(res)
else:
    if res[first_odd] == chr(43):
         print(res[:first_odd] + chr(43) + res[first_odd + 1:])
    else:
        print(res)




# '+'
# '×'

