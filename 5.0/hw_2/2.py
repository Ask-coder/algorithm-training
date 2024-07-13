#! /usr/bin/env python3
# -*- codign: utf-8 -*-

N, K = map(int, input().split())
data = list(map(int, input().split()))

def get_max_profit(N, K, data):
    res = 0
    for i in range(N):
        j = 0
        while j <= K and i + j < N:
            res = max(res, data[i + j] - data[i])
            j += 1
    return res

print(get_max_profit(N, K, data))

