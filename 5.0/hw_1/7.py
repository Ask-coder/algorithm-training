#! /usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input())
y = int(input())
p = int(input())

res = 0
enemy = 0 # солдаты противника
# y - здоровье казармы
# x - наши солдаты
# p - сколько производит солдат казарма противника
#
while x > 0 and (enemy > 0 or y > 0):
    res += 1
    # остаток солдат собственных после нападения проивника
    domage = x - enemy
    # Если остались солдаты
    if domage > 0:
        # забрать здоровье у казармы
        y -= domage
        # обнулить вражескую армию
        enemy = 0
    # солдат не осталось
    else:
        if y <= x:
            enemy -= x - y
            y = 0
        else:
            y -= x

    if enemy <= 0 and y <= 0:
        # print(res)
        break
    x -= enemy
    if x <= 0:
        res = -1
        break
    if y > 0:
        enemy += p

print(res)
