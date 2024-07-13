#! /usr/bin/env python3
# -*- codfing: utf-8 -*-

n = int(input())
arr = [input() for _ in range(n)]
rang = 10
length = len(arr[0])

print("Initial array:")
print(", ".join(arr))
print("*" * 10)

for i in range(length):
    buckets = [[] for i in range(rang)]
    for x in arr:
        buckets[int(x) // 10 ** i % 10].append(x)

    arr = []
    print(f"Phase {i + 1}")
    for i in range(rang):
        arr += buckets[i]
        print(f"Bucket {i}: {(', '.join(buckets[i])) or 'empty'}")
    print("*" * 10)

print("Sorted array:")
print(", ".join(arr))

