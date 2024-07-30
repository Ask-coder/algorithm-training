import math

n = int(input())
tshorts = list(map(int, input().split()))
m = int(input())
throusers = list(map(int, input().split()))

myMin =  math.inf
i = j = 0
idx_tshorts = idx_throusers = -1

while i < n and j < m:
    diff = abs(tshorts[i] - throusers[j])

    if myMin > diff:
        myMin = diff
        idx_throusers = j
        idx_tshorts = i

    if tshorts[i] < throusers[j]:
        i += 1
    else:
        j += 1 

print(tshorts[idx_tshorts], throusers[idx_throusers])