#! /usr/bin/env python3
#! -*- coding: utf-8 -*-


def merge(a, l1, r1, l2, r2, curr, aux):
    k = i = l1
    j = l2
    while i <= r1 and j <= r2:
        if a[i] < a[j]:
            aux[k] = a[i]
            i += 1
        else:
            aux[k] = a[j]
            j += 1
        k += 1
    aux[k:r2 + 1] = a[i:r1 + 1] or a[j:r2 + 1]



def merge_sort(res, l, r, arr):
    if l >= r:
        return
    mid =  (l + r)  // 2
    merge_sort(arr, l, mid, res)
    merge_sort(arr, mid + 1, r, res)
    merge(res, l, mid, mid + 1, r, curr, arr)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    res = arr[:]
    curr = 0
    merge_sort(res, 0, n - 1, arr)
    print(" ".join(list(map(str, arr))))

