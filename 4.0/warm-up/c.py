#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import math


def func(x_a, y_a, x_b, y_b):
    r_a = (x_a ** 2 + y_a ** 2) ** 0.5
    r_b = (x_b ** 2 + y_b ** 2) ** 0.5
    angle_a = math.atan2(y_a, x_a)
    angle_b = math.atan2(y_b, x_b)
    if angle_a < 0:
        angle_a += 2 * math.pi
    if angle_b < 0:
        angle_b += 2 * math.pi
    angle = abs(angle_a - angle_b)
    if angle > math.pi:
        angle -= math.pi * 2

    arc_length = r_b * abs(angle) + abs(r_a - r_b)
    return min(r_a + r_b, arc_length)

if __name__ == "__main__":
    x_a, y_a, x_b, y_b = map(int, input().split())
    print(f"{func(x_a, y_a, x_b, y_b):.12f}")


