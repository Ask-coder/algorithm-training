n = int(input())
arr = list(map(int, input().split()))
x = int(input())

def lbinsearch(arr, x):
    l = 0
    r = len(arr)
    while l < r:
        m = (l + r) // 2
        if x > arr[m]:
            l = m + 1
        else:
            r = m
    return l

idx = lbinsearch(arr, x)
print(idx)

            
