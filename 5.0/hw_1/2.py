#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# G1_1, G2_1 = 1, 2
# G1_2, G2_2 = 3, 4
G1_1, G2_1 = map(int, input().split(':'))
G1_2, G2_2 = map(int, input().split(':'))
IS_HOME = int(input())
res = 0

G1 = G1_1 + G1_2
G2 = G2_1 + G2_2

G1_visited = G1_2 if IS_HOME == 1 else G1_1
G2_visited = G2_1 if IS_HOME == 1 else G2_2

if G2 > G1:
    res = G2 - G1
    if IS_HOME == 1:
        G1_visited += res
    if G2_visited >= G1_visited:
        res += 1

elif G1 == G2:
    if G2_visited >= G1_visited:
        res += 1

print(res)
