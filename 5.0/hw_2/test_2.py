#! /usr/bin/env python3
# -*- codign: utf-8 -*-
# from 2 import get_max_profit
# N, K = map(int, input().split())
# data = [int(input()) for i in range(N)]


def get_max_profit(N, K, data):
    res = 0
    for i in range(N):
        j = 0
        tmp = set()
        while j <= K and i + j < N:
            res = max(res, data[i + j] - data[i])
            j += 1
    return res


def test_answer():
    assert get_max_profit(5, 2, [1, 2, 3, 4, 5]) == 2
    assert get_max_profit(5, 2, [5, 4, 3, 2, 1]) == 0


