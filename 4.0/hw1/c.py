#! /usr/bin/env python3
# -*- codign: utf-8 -*-
#
def merge(l1, r1, a1, l2, r2, a2,  curr, result):
    while l1 < r1 and l2 < r2:
        if a1[l1] <= a2[l2]:
            result.append(a1[l1])
            l1 += 1
            curr += 1
        else:
            result.append(a2[l2])
            l2 += 1
            curr += 1

    result += a1[l1:]
    curr += r1 - l1
    result += a2[l2:]
    curr += r2 - l2


if __name__ == "__main__":
    n = int(input())
    arr_1 = list(map(int, input().split()))
    m = int(input())
    arr_2 = list(map(int, input().split()))
    result = []
    merge(0, n, arr_1, 0, m, arr_2, 0, result)
    print(" ".join(list(map(str, result))))
