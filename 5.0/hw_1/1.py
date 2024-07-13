#! /usr/bin/env python3
# -*- coding: utf-8 -*-

P, V = map(int, input().split())
Q, M = map(int, input().split())
#
line_1 = (P - V, P + V)
line_2 = (Q - M, Q + M)

left = max(line_1[0], line_2[0])
right = min(line_1[1], line_2[1])

# Отрезки пересклись
if right > left:
    res = max(line_1[1], line_2[1]) - min(line_1[0], line_2[0]) + 1
# у отрезков одна общая точка
elif left == right:
    res = max(line_1[1], line_2[1]) - min(line_1[0], line_2[0]) + 1
# Отрезки не пересекаются
else:
    res = abs(line_1[1] - line_1[0]) + abs(line_2[1] - line_2[0]) + 2

print(res)
# print(max(P + V, Q + M) - min(P - V, Q - M) + 1)
