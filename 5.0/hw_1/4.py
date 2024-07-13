#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#

R = [] # ладья бьёт по вертикали и горизонтали
B = [] # слон бьёт по диагонали

figures = set()
fight = set()
for i in range(8):
    line = input()[:8]
    for j in range(len(line)):
        if line[j] == 'R':
            R.append((i, j))
            figures.add((i, j))
        elif line[j] == 'B':
            B.append((i, j))
            figures.add((i, j))

for item in R:
    for i in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        x = item[0]
        y = item[1]
        while 0 <= x + i[0] < 8 and 0 <= y + i[1] < 8 and (x + i[0], y + i[1]) not in figures:
            x += i[0]
            y += i[1]
            fight.add((x, y))
for item in B:
    for i in [(-1, -1), (1, 1), (-1, 1), (1, -1)]:
        x = item[0]
        y = item[1]
        while 0 <= x + i[0] < 8 and 0 <= y + i[1] < 8 and (x + i[0], y + i[1]) not in figures:
            x += i[0]
            y += i[1]
            fight.add((x, y))

print(8 * 8 - len(fight) - len(figures))
