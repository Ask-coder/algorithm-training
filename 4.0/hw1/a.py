#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def partition(l, r, x, a):
    curr = lt = l
    gt = r - 1
    while curr <= gt:
        print(f"curr = {curr}, lt = {lt}, gt = {gt}")
        if a[curr] < x:
            a[curr], a[lt] = a[lt], a[curr]
            curr += 1
            lt += 1
        elif a[curr] > x:
            a[curr], a[gt] = a[gt], a[curr]
            gt -= 1
        else:
            curr += 1
        print(a)
    return lt


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    pivot = int(input())
    lt = partition(0, n, pivot, arr)
    print(lt)
    print(n - lt)



