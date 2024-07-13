#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def partition(l, r, a, x):
    E = G = l
    for N in range(l, r):
        if a[N] < x:
            tmp = a[N]
            a[N] = a[G]
            a[G] = a[E]
            a[E] = tmp
            E += 1
            G += 1
        elif a[N] == x:
            a[N], a[G] = a[G], a[N]
            G += 1
    return E, G

def quick_sort(l, r, a):
    if r - l < 2:
        return
    # выбрать опорный элемент
    pivot = a[random.randint(l, r - 1)]
    e, g = partition(l, r, a, pivot)
    quick_sort(l, e, a)
    quick_sort(g, r, a)




if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    quick_sort(0, n, arr)
    print(" ".join(list(map(str, arr))))
